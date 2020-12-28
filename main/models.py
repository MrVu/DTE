from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.html import mark_safe


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
        verbose_name_plural = 'Khách hàng'


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=20, blank=True,
                                choices=[('Consultant', 'Consultant'), ('Sale', 'Sale'), ('Manager', 'Manager')])
    profilePic = models.ImageField(null=True)

    class Meta:
        verbose_name = 'Thành viên'
        verbose_name_plural = 'Thành viên'


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
    subjectName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.subjectName

    class Meta:
        verbose_name = 'Môn học'
        verbose_name_plural = 'Môn học'


class University(models.Model):
    universityName = models.CharField(max_length=200, null=True)
    subjects = models.ManyToManyField(Subject, related_name='universities')
    description = models.TextField(null=True)
    pic = models.ImageField(null=True)

    def __str__(self):
        return self.universityName

    class Meta:
        verbose_name = 'Trường'
        verbose_name_plural = 'Trường'


class Level(models.Model):
    levelName = models.CharField(max_length=200, null=True,
                                 choices=[('Đại học', 'Đại học'), ('Sau đại học', 'Sau đại học'),
                                          ('Thạc sĩ', 'Thạc sĩ')])
    feeAYear = models.IntegerField(null=True)
    ieltOverall = models.FloatField(null=True, choices=(
        ('', 'IELTS Overall'), (4, '4.0'), (4.5, '4.5'), (5, '5.0'), (5.5, '5.5'), (6, '6.0'), (6.5, '6.5'),
        (7, '7.0')))
    ieltsMin = models.FloatField(null=True, choices=(
        ('', 'IELTS Minumum'), (4, '4.0'), (4.5, '4.5'), (5, '5.0'), (5.5, '5.5'), (6, '6.0'), (6.5, '6.5'),
        (7, '7.0')))
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.levelName


class GuestCustomer(models.Model):
    subject = models.CharField(max_length=200, null=True)
    guest_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    ielts_overall = models.CharField(max_length=20, null=True, choices=(
        ('', 'IELTS trung bình'), ('4', '4.0'), ('4.5', '4.5'), ('5', '5.0'), ('5.5', '5.5'), ('6', '6.0'),
        ('6.5', '6.5'),
        ('7', '7.0')))
    ielts_min = models.CharField(max_length=20, null=True, choices=(
        ('', 'IELTS thấp nhất'), ('4', '4.0'), ('4.5', '4.5'), ('5', '5.0'), ('5.5', '5.5'), ('6', '6.0'),
        ('6.5', '6.5'),
        ('7', '7.0')))
    level = models.CharField(max_length=50, null=True,
                             choices=[('Đại học', 'Đại học'), ('Sau đại học', 'Sau đại học'), ('Thạc sĩ', 'Thạc sĩ')])

    def __str__(self):
        return self.guest_name

    class Meta:
        verbose_name = 'Khách vãng lai'
        verbose_name_plural = 'Khách vãng lai'
