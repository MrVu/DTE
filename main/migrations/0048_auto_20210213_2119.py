# Generated by Django 3.1.4 on 2021-02-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20210213_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show_on_homepage',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='show_on_homepage',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
