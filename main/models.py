from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField
from django.template.defaultfilters import slugify


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
        verbose_name_plural = 'Quản trị viên'


class Subject(models.Model):
    subjectName = models.CharField(
        max_length=200, null=True, verbose_name='Tên ngành')
    pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.subjectName

    class Meta:
        verbose_name = 'Nhóm ngành'
        verbose_name_plural = 'Quản lý nhóm ngành'
        ordering = ['subjectName']


class UniSubject(models.Model):
    name = models.CharField(max_length=200, null=True,
                            verbose_name='Tên khóa học')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Khóa học'
        verbose_name_plural = 'Quản lý Khóa học'
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
    show_on_homepage = models.BooleanField(null=True, default=False)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.universityName

    class Meta:
        verbose_name = 'Trường'
        verbose_name_plural = 'Quản lý trường'
        ordering = ['universityName']

    def save(self, *args, **kwargs):  # add slug on save event
        if not self.slug:
            self.slug = slugify(self.universityName)
        return super().save(*args, **kwargs)


class Scholarship(models.Model):
    name = models.CharField(max_length=200, null=True)
    value = models.IntegerField(null=True)
    time = models.CharField(max_length=200)
    uni = models.ForeignKey(University, on_delete=models.CASCADE)


class Level(models.Model):
    level_choices = [('gcse', 'THCS'), ('a-level-foundation', 'Dự bị đại học'), ('under-graduate', 'Đại học'),
                     ('graduate', 'Thạc sĩ-Master'),
                     ('research', 'Tiến sĩ-Nghiên cứu-Trợ lý giáo sư')]
    ielts_choices = [
        ('', 'IELTS Overall'), (4.0, '4.0'), (4.5, '4.5'), (5.0,
                                                            '5.0'), (5.5, '5.5'), (6.0, '6.0'), (6.5, '6.5'),
        (7.0, '7.0')]
    name = models.CharField(max_length=200, null=True,
                            choices=level_choices)
    feeAYear = models.IntegerField(null=True)
    ielts_overall = models.FloatField(null=True, choices=ielts_choices)
    ieltsMin = models.FloatField(null=True, choices=ielts_choices)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return ''


class Article(models.Model):
    img_description = models.ImageField(null=True)
    title = models.CharField(max_length=200, null=True)
    body = RichTextField(null=True)
    date = models.DateTimeField(default=datetime.now, null=True)
    cropping = ImageRatioField('img_description', '450x350 ')
    show_on_homepage = models.BooleanField(null=True, default=False)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bài viết'
        verbose_name_plural = 'Quản lý bài viết'

    def save(self, *args, **kwargs):  # add slug on save event
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class PageInfo(models.Model):
    page_name = models.CharField(max_length=50, null=True)
    logo = models.ImageField(null=True)
    facebook_url = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'Thông tin website'
        verbose_name_plural = 'Quản lý thông tin website'

    def __str__(self):
        return self.page_name


class Banner(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=200, null=True)
    img = models.ImageField(null=True)
    page = models.ForeignKey(PageInfo, on_delete=models.CASCADE)
    cropping = ImageRatioField('img', '1400x600')


class CustomerComment(models.Model):
    img = models.ImageField(null=True)
    name = models.CharField(max_length=200, null=True)
    school = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=200, null=True)
    page = models.ForeignKey(PageInfo, on_delete=models.CASCADE)
    cropping = ImageRatioField('img', '140x140')


class CompanyAddress(models.Model):
    title = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    page = models.ForeignKey(PageInfo, on_delete=models.CASCADE)
