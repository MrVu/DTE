"""DTE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('universities/', views.universities, name='universities'),
    path('uni-search-result', views.uni_search_result, name='uni_search_result'),
    path('universities/<int:university_id>',
         views.university_detail, name='university_detail'),
    path('uni-by-subject/<int:uni_subject_id>', views.universities_by_subject, name='uni_by_subject'),
    path('level/<str:level>', views.universities_by_level, name='universities_by_level'),
    path('subjects/', views.subjects_query, name='subjects_query'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:article_id>', views.article_detail, name='article_detail'),
    path('contact/', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
