# Generated by Django 3.1.4 on 2021-01-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20210103_0348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageinfo',
            options={'verbose_name': 'Thông tin website', 'verbose_name_plural': 'Quản lý thông tin website'},
        ),
        migrations.AddField(
            model_name='pageinfo',
            name='team_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
