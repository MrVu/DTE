from django.shortcuts import render
from .models import Customer, User, Tracking, University, Level, Subject, Article, PageInfo
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.response import Response
from .forms import GuestCustomerForm
from django.db.models import Q


# Create your views here.


def index(request):
    universities = University.objects.all()[:3]
    articles = Article.objects.all()[:3]
    return render(request, 'main/index.html', context={'universities': universities, 'articles': articles})


def universitiesFilter(request):
    form = GuestCustomerForm()
    unies = None
    page_name = 'Tìm trường'
    if request.method == 'POST':
        form = GuestCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            unies = University.objects.filter(subjects=form.cleaned_data['subject']).filter(
                cities=form.cleaned_data['cities']).filter(Q(level__levelName=form.cleaned_data['level']) & Q(
                level__feeAYear__lte=form.cleaned_data['budget']))
            print(unies)
    return render(request, 'main/universitiesFilter.html',
                  context={'unies': unies, 'form': form, 'page_name': page_name})


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
    arts = Article.objects.all()
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
