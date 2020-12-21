from django.shortcuts import render
from .models import Customer, JobAvailable, User, Tracking
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.
def trackingUser(user, path):
    tracking = Tracking.objects.create(userName=user.username, request=path)
    tracking.save()

@login_required
def index(request):
    test = 20
    return render(request, 'main/index.html', context={'test': test})

@login_required
def customers(request):
    trackingUser(request.user, request.get_full_path())
    pageName='customers'
    customers = Customer.objects.all()
    tableHeader = ['ID','Full Name', 'Phone Number', 'Current Job', 'Status']
    return render(request, 'main/table.html', context={'customers': customers, 'tableHeader': tableHeader, 'pageName':pageName})

@login_required
def customerDetail(request, customer_id):
    trackingUser(request.user, request.get_full_path())
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'main/customer.html', context={'customer': customer})

@login_required
def availableJobs(request):
    trackingUser(request.user, request.get_full_path())
    pageName='jobs'
    jobs = JobAvailable.objects.all()
    tableHeader = ['Country', 'Position', 'Education','IELTS', 'Available']
    return render(request, 'main/table.html', context={'jobs':jobs, 'tableHeader': tableHeader, 'pageName':pageName})

@login_required
def userDetail(request, userId):
    user = User.objects.get(id=userId)
    return render(request, 'main/user.html',context={'user': user})

@login_required
def fitJobs(request, customer_id):
    trackingUser(request.user, request.get_full_path())
    pageName='fitJobs'
    customer = Customer.objects.get(id=customer_id)
    jobs = JobAvailable.objects.filter(budget__lte=customer.budget).filter(ielts__lte=customer.ielts).filter(education__lte=customer.education).filter(available__gte=0)
    tableHeader = ['Country', 'Position', 'Education','IELTS', 'Available']
    return render(request, 'main/table.html', context={'customer': customer,'jobs':jobs, 'tableHeader': tableHeader, 'pageName':pageName})

@login_required
def tracking(request):
    pageName = 'tracking'
    tracks = Tracking.objects.order_by('-date')
    tableHeader= ['Tên người dùng', 'Trang', 'Thời gian']
    return render(request, 'main/table.html', context={'tracks': tracks, 'tableHeader': tableHeader, 'pageName':pageName})
