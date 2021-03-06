# Generated by Django 3.1.4 on 2021-02-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_auto_20210213_2119'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='GuestCustomer',
        ),
        migrations.DeleteModel(
            name='SaleSummary',
        ),
        migrations.DeleteModel(
            name='Tracking',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Nhân viên', 'verbose_name_plural': 'Quản trị viên'},
        ),
        migrations.RemoveField(
            model_name='pageinfo',
            name='feature_uni_baner',
        ),
        migrations.RemoveField(
            model_name='pageinfo',
            name='team_description',
        ),
        migrations.RemoveField(
            model_name='pageinfo',
            name='team_pic',
        ),
        migrations.AddField(
            model_name='university',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
