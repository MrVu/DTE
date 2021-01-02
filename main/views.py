from django.shortcuts import render
from .models import Customer, User, Tracking, University, Level, Subject, Article
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.response import Response
from .forms import GuestCustomerForm
from django.db.models import Q


# Create your views here.
def trackingUser(user, path):
    tracking = Tracking.objects.create(userName=user.username, request=path)
    tracking.save()


def index(request):
    universities = University.objects.all()[:3]
    articles = Article.objects.all()[:3]
    return render(request, 'main/index.html', context={'universities': universities, 'articles': articles})


def universitiesFilter(request):
    form = GuestCustomerForm()
    unies = None
    if request.method == 'POST':
        form = GuestCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            unies = University.objects.filter(subjects=form.cleaned_data['subject']).filter(
                cities=form.cleaned_data['cities']).filter(Q(level__levelName=form.cleaned_data['level']) & Q(
                level__feeAYear__lte=form.cleaned_data['budget']))
            print(unies)
    return render(request, 'main/universitiesFilter.html',
                  context={'unies': unies, 'form': form})


def universities(request):
    universities = University.objects.all()
    return render(request, 'main/universities.html', context={'universities': universities})


def university_detail(request, university_id):
    university = University.objects.get(id=university_id)
    subjects = Subject.objects.filter(universities=university)
    return render(request, 'main/uni_detail.html', context={'university': university, 'subjects': subjects})


@login_required
def userDetail(request, userId):
    user = User.objects.get(id=userId)
    return render(request, 'main/user.html', context={'user': user})


@login_required
def tracking(request):
    pageName = 'tracking'
    tracks = Tracking.objects.order_by('-date')
    tableHeader = ['Tên người dùng', 'Trang', 'Thời gian']
    return render(request, 'main/table.html',
                  context={'tracks': tracks, 'tableHeader': tableHeader, 'pageName': pageName})
