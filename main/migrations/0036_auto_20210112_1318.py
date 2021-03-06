# Generated by Django 3.1.4 on 2021-01-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20210112_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestcustomer',
            name='uni_subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='guestcustomer',
            name='city_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='ieltsMin',
            field=models.FloatField(choices=[('', 'IELTS Overall'), (4.0, '4.0'), (4.5, '4.5'), (5.0, '5.0'), (5.5, '5.5'), (6.0, '6.0'), (6.5, '6.5'), (7.0, '7.0')], null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subjectName',
            field=models.CharField(max_length=200, null=True, verbose_name='Tên ngành'),
        ),
        migrations.AlterField(
            model_name='unisubject',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Tên khóa học'),
        ),
        migrations.AlterField(
            model_name='university',
            name='subjects',
            field=models.ManyToManyField(related_name='universities', to='main.Subject', verbose_name='Ngành học'),
        ),
        migrations.AlterField(
            model_name='university',
            name='uni_subjects',
            field=models.ManyToManyField(to='main.UniSubject', verbose_name='Môn học'),
        ),
        migrations.AlterField(
            model_name='university',
            name='universityName',
            field=models.CharField(max_length=200, null=True, verbose_name='Tên trường'),
        ),
    ]
