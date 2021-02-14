from django.shortcuts import render
from .models import User, University, Level, Subject, Article, PageInfo, UniSubject
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    universities = University.objects.filter(show_on_homepage=True)
    return render(request, 'main/index.html',
                  context={'universities': universities})


def uni_search(request):
    guest_email = request.POST.get('email')
    if guest_email:
        guest = GuestCustomer.objects.filter(email=guest_email).first()
    else:
        guest = None
    form = GuestCustomerForm(instance=guest)
    page_name = 'Tìm khóa học'
    unies = None
    if request.method == 'POST':
        form = GuestCustomerForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            request.session['subject'] = form.cleaned_data['subject'].subjectName
            request.session['level'] = form.cleaned_data['level']
            return HttpResponseRedirect(reverse('additional_step'))
    return render(request, 'main/uni_search.html',
                  context={'unies': unies, 'form': form, 'page_name': page_name})


def additional_search(request):
    if 'city' in request.session:
        del request.session['city']
    if 'uni_subject' in request.session:
        del request.session['uni_subject']
    if not 'subject' and not 'level' in request.session:
        return HttpResponseRedirect(reverse('uni_search'))
    else:
        page_name = 'Tìm chi tiết'
        form = AdditionalStepForm(request=request)
        if request.method == 'POST':
            form = AdditionalStepForm(request.POST, request=request)
            if form.is_valid():
                if form.cleaned_data['city']:
                    request.session['city'] = form.cleaned_data['city'].city_name
                if form.cleaned_data['uni_subject']:
                    request.session['uni_subject'] = form.cleaned_data['uni_subject'].name
                return HttpResponseRedirect(reverse('uni_search_result'))
            else:
                return HttpResponseRedirect(reverse('uni_search_result'))
        return render(request, 'main/additional_step.html', context={'form': form})


def uni_search_result(request):
    page_name = 'Kết quả tìm kiếm'
    if 'subject' in request.session and 'level' in request.session:
        if 'city' in request.session and not 'uni_subject' in request.session:
            universities = University.objects.filter(Q(subjects__subjectName=request.session.get(
                'subject')) & Q(level__name=request.session.get('level')) & Q(
                cities__city_name=request.session.get('city')))
        elif 'uni_subject' in request.session and not 'city' in request.session:
            universities = University.objects.filter(Q(subjects__subjectName=request.session.get(
                'subject')) & Q(level__name=request.session.get('level')) & Q(
                uni_subjects__name=request.session.get('uni_subject')))
        elif 'city' in request.session and 'uni_subject' in request.session:
            universities = University.objects.filter(Q(subjects__subjectName=request.session.get(
                'subject')) & Q(level__name=request.session.get('level')) & Q(
                cities__city_name=request.session.get('city')) & Q(
                uni_subjects__name=request.session.get('uni_subject')))
        else:
            universities = University.objects.filter(Q(subjects__subjectName=request.session.get(
                'subject')) & Q(level__name=request.session.get('level')))
        if not universities:
            message = "Không tìm thấy trường phù hợp với bạn"
            header = ""
        else:
            message = ""
            header = "Trường phù hợp với bạn"
        return render(request, 'main/uni_search_result.html',
                      context={'universities': universities, 'page_name': page_name, 'message': message,
                               'header': header})
    else:
        return HttpResponseRedirect(reverse('uni_search'))


def universities_by_subject(request, uni_subject_id):
    uni_subject = UniSubject.objects.get(id=uni_subject_id)
    universities = University.objects.filter(uni_subjects=uni_subject)
    page_name = 'Khóa học'
    message = ""
    header = f"Có {universities.count()} trường có khóa học {uni_subject.name}"
    return render(request, 'main/uni_search_result.html',
                  context={'universities': universities, 'page_name': page_name, 'message': message,
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
    return render(request, 'main/subjects.html', context={'page_name': page_name, 'subjects': subjects})


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
    page_name = 'Đọc bài viết'
    return render(request, 'main/article_detail.html', context={'art': art, 'page_name': page_name})


def contact(request):
    page_name = 'Liên hệ'
    return render(request, 'main/contact.html', context={'page_name': page_name})


def about_us(request):
    page_name = 'Lịch sử phát triển'
    return render(request, 'main/about_us.html', context={'page_name': page_name})
