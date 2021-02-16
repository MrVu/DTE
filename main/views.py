from django.shortcuts import render
from .models import User, University, Level, Subject, Article, PageInfo, UniSubject
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm, SearchForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def index(request):
    universities = University.objects.filter(show_on_homepage=True)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            request.session['subject'] = form.cleaned_data['subject'].subjectName
            request.session['level'] = form.cleaned_data['level']
            return redirect('uni_search_result')
    return render(request, 'main/index.html',
                    context={'universities': universities})




def uni_search_result(request):
    page_name = 'Kết quả tìm kiếm'
    if 'subject' in request.session and 'level' in request.session:
        universities = University.objects.filter(level__name=request.session.get('level')).filter(subjects__subjectName=request.session.get('subject')).distinct()
        paginator = Paginator(universities, 8) # Show 8 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if not universities:
            message = "Không tìm thấy trường phù hợp với bạn"
            header = ""
        else:
            message = ""
            header = "Trường phù hợp với bạn"
        return render(request, 'main/uni_search_result.html',
                      context={'page_obj': page_obj, 'page_name': page_name, 'message': message,
                               'header': header})
    else:
        return HttpResponseRedirect(reverse('uni_search'))


def universities_by_subject(request, uni_subject_id):
    uni_subject = UniSubject.objects.get(id=uni_subject_id)
    universities = University.objects.filter(uni_subjects=uni_subject)
    page_name = 'Khóa học'
    message = ""
    header = f"Có {universities.count()} trường có khóa học {uni_subject.name}"
    paginator = Paginator(universities, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/uni_search_result.html',
                  context={'page_obj': page_obj, 'page_name': page_name, 'message': message,
                           'header': header})

def universities_by_level(request, level):
    universities = University.objects.filter(level__name=level).all()
    paginator = Paginator(universities, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_name = 'Danh sách trường phù hợp'
    return render(request, 'main/universities.html', context={'page_obj': page_obj, 'page_name': page_name})


def subjects_query(request):
    page_name = 'Danh sách ngành học'
    subjects = Subject.objects.filter(unisubject__isnull=False).distinct()
    paginator = Paginator(subjects, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/subjects.html', context={'page_name': page_name, 'page_obj': page_obj})


def universities(request):
    universities = University.objects.all()
    paginator = Paginator(universities, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_name = 'Danh sách trường'
    return render(request, 'main/universities.html', context={'page_obj': page_obj, 'page_name': page_name})


def university_detail(request, university_id):
    university = University.objects.get(id=university_id)
    page_name = university.universityName
    return render(request, 'main/uni_detail.html',
                  context={'university': university, 'page_name': page_name})


def articles(request):
    articles = Article.objects.filter(show_on_homepage=False).order_by('-date')
    paginator = Paginator(articles, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_name = 'Tin tức'
    return render(request, 'main/articles.html', context={'page_obj': page_obj, 'page_name': page_name})


def article_detail(request, article_id):
    art = Article.objects.get(id=article_id)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Tư vấn khách hàng'
            message = 'Tên khách hàng: ' + form.cleaned_data['name'] +'\n' + 'Email: ' + form.cleaned_data['email'] + '\n' + 'Điện thoại: ' + form.cleaned_data['phone_number'] + '\n' + 'Nội dung: ' + form.cleaned_data['message'] 
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['vuhoang17891@gmail.com']
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Yêu cầu của bạn đã được gửi')
        return redirect('article_detail', article_id=art.id)
    page_name = 'Đọc bài viết'
    return render(request, 'main/article_detail.html', context={'form':form,'art': art, 'page_name': page_name})


def contact(request):
    page_name = 'Liên hệ'
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Tư vấn khách hàng'
            message = 'Tên khách hàng: ' + form.cleaned_data['name'] +'\n' + 'Email: ' + form.cleaned_data['email'] + '\n' + 'Điện thoại: ' + form.cleaned_data['phone_number'] + '\n' + 'Nội dung: ' + form.cleaned_data['message'] 
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['vuhoang17891@gmail.com']
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Yêu cầu của bạn đã được gửi')
        return HttpResponseRedirect(reverse('contact'))
    return render(request, 'main/contact.html', context={'page_name': page_name, 'form': form})

