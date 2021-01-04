from django.shortcuts import render
from .models import Customer, User, Tracking, University, Level, Subject, Article, PageInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import GuestCustomerForm
from django.db.models import Q


# Create your views here.


def index(request):
    universities = University.objects.all()[:3]
    articles = Article.objects.order_by('-date')[:3]
    return render(request, 'main/index.html', context={'universities': universities, 'articles': articles})


def uni_search(request):
    form = GuestCustomerForm()
    page_name = 'Tìm trường'
    unies = None
    if request.method == 'POST':
        form = GuestCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['subject'] = form.cleaned_data['subject'].subjectName
            request.session['city_name'] = form.cleaned_data['city_name'].city_name
            request.session['level'] = form.cleaned_data['level']
            request.session['budget'] = form.cleaned_data['budget']
            return HttpResponseRedirect(reverse('uni_search_result'))
    return render(request, 'main/uni_search.html',
                  context={'unies': unies, 'form': form, 'page_name': page_name})


def uni_search_result(request):
    page_name = 'Kết quả tìm kiếm'
    if 'subject' and 'city_name' and 'level' and 'budget' in request.session:
        unies = University.objects.filter(subjects__subjectName=request.session.get('subject')).filter(
            cities__city_name=request.session.get('city_name')).filter(
            Q(level__levelName=request.session.get('level')) & Q(
                level__feeAYear__lte=request.session.get('budget')))
        return render(request,'main/uni_search_result.html', context={'unies': unies, 'page_name': page_name})
    else:
        return HttpResponseRedirect(reverse('uni_search'))


def universities(request):
    universities = University.objects.all()
    page_name = 'Danh sách trường'
    return render(request, 'main/universities.html', context={'universities': universities, 'page_name': page_name})


def university_detail(request, university_id):
    university = University.objects.get(id=university_id)
    page_name = university.universityName
    subjects = Subject.objects.filter(universities=university)
    return render(request, 'main/uni_detail.html',
                  context={'university': university, 'subjects': subjects, 'page_name': page_name})


def articles(request):
    arts = Article.objects.order_by('-date')
    page_name = 'Bài viết'
    return render(request, 'main/articles.html', context={'arts': arts, 'page_name': page_name})


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
