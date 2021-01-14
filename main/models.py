from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField


# Create your models here.
class SaleSummary(models.Model):
    class Meta:
        verbose_name = 'Sale Summary'
        verbose_name_plural = 'Sales Summary'


class Customer(models.Model):
    fullName = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    phoneNumber = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    ielts = models.FloatField(null=True)
    budget = models.BigIntegerField(null=True)
    currentJob = models.CharField(max_length=200, null=True)
    education = models.IntegerField(null=True)
    status = models.CharField(max_length=200, null=True,
                              choices=[('Contact', 'Contact'), ('Pending', 'Pending'), ('Done', 'Done')])
    exp = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    profilePic = models.ImageField()

    @property
    def thumbnail_preview(self):
        if self.profilePic:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.profilePic.url))
        return ""

    def __str__(self):
        return self.fullName

    class Meta:
        verbose_name = 'Khách hàng'
        verbose_name_plural = 'Quản lý khách hàng'


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=20, blank=True,
                                choices=[('Consultant', 'Consultant'), ('Sale', 'Sale'), ('Manager', 'Manager')])
    profilePic = models.ImageField(null=True)

    class Meta:
        verbose_name = 'Nhân viên'
        verbose_name_plural = 'Quản lý nhân viên'


class Tracking(models.Model):
    userName = models.CharField(max_length=50)
    request = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.userName

    class Meta:
        verbose_name = 'Theo dõi'
        verbose_name_plural = 'Theo dõi'


class Subject(models.Model):
    subjectName = models.CharField(
        max_length=200, null=True, verbose_name='Tên ngành')

    def __str__(self):
        return self.subjectName

    class Meta:
        verbose_name = 'Nhóm ngành'
        verbose_name_plural = 'Quản lý nhóm ngành'
        ordering =['subjectName']


class UniSubject(models.Model):
    name = models.CharField(max_length=200, null=True,
                            verbose_name='Tên khóa học')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Ngành nhỏ'
        verbose_name_plural = 'Quản lý ngành nhỏ'
        ordering = ['name']


class City(models.Model):
    city_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = 'Thành phố'
        verbose_name_plural = 'Thành phố'
        ordering = ['city_name']


class University(models.Model):
    universityName = models.CharField(
        max_length=200, null=True, verbose_name='Tên trường')
    cities = models.ManyToManyField(City)
    subjects = models.ManyToManyField(
        Subject, related_name='universities', verbose_name='Ngành học')
    uni_subjects = models.ManyToManyField(UniSubject, verbose_name='Môn học')
    description = RichTextField(null=True)
    pic = models.ImageField(null=True)
    cropping = ImageRatioField('pic', '370x240')

    def __str__(self):
        return self.universityName

    class Meta:
        verbose_name = 'Trường'
        verbose_name_plural = 'Quản lý trường'
        ordering = ['universityName']


class Scholarship(models.Model):
    name = models.CharField(max_length=200, null=True)
    value = models.IntegerField(null=True)
    time = models.CharField(max_length=200)
    uni = models.ForeignKey(University, on_delete=models.CASCADE)


class Level(models.Model):
    level_choices = [('Đại học', 'Đại học'), ('Sau đại học', 'Sau đại học'),
                     ('Thạc sĩ', 'Thạc sĩ')]
    ielts_choices = [
        ('', 'IELTS Overall'), (4.0, '4.0'), (4.5, '4.5'), (5.0,
                                                            '5.0'), (5.5, '5.5'), (6.0, '6.0'), (6.5, '6.5'),
        (7.0, '7.0')]
    levelName = models.CharField(max_length=200, null=True,
                                 choices=level_choices)
    feeAYear = models.IntegerField(null=True)
    ielts_overall = models.FloatField(null=True, choices=ielts_choices)
    ieltsMin = models.FloatField(null=True, choices=ielts_choices)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.levelName


class GuestCustomer(models.Model):
    subject = models.CharField(max_length=200, null=True)
    city_name = models.CharField(max_length=200, null=True, blank=True)
    guest_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    level = models.CharField(max_length=50, null=True,
                             choices=[('Đại học', 'Đại học'), ('Sau đại học', 'Sau đại học'), ])
    date = models.DateTimeField(default=datetime.now, null=True)
    uni_subject = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.guest_name

    class Meta:
        verbose_name = 'Khách vãng lai'
        verbose_name_plural = 'Quản lý Khách vãng lai'


class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = RichTextField(null=True)
    date = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bài viết'
        verbose_name_plural = 'Quản lý bài viết'


class PageInfo(models.Model):
    page_name = models.CharField(max_length=50, null=True)
    logo = models.ImageField(null=True)
    address = models.CharField(max_length=200, null=True)
    address_2 = models.CharField(max_length=200, null=True)
    address_3 = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    facebook_url = models.CharField(max_length=200, null=True)
    banner = models.ImageField(null=True)
    banner_slogan_title_1 = models.CharField(max_length=200, null=True)
    banner_slogan_1 = models.CharField(max_length=200, null=True)
    banner_slogan_title_2 = models.CharField(max_length=200, null=True)
    banner_slogan_2 = models.CharField(max_length=200, null=True)
    banner_slogan_title_3 = models.CharField(max_length=200, null=True)
    banner_slogan_3 = models.CharField(max_length=200, null=True)
    feature_uni_baner = models.ImageField(null=True)
    team_pic = models.ImageField(null=True)
    team_description = RichTextField(null=True)
    cropping = ImageRatioField('banner', '1200x420')


    class Meta:
        verbose_name = 'Thông tin website'
        verbose_name_plural = 'Quản lý thông tin website'

    def __str__(self):
        return self.page_name
