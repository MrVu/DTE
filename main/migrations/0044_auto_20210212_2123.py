# Generated by Django 3.1.4 on 2021-02-12 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20210212_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customercomment',
            old_name='comment',
            new_name='body',
        ),
    ]
