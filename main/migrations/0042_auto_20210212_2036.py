# Generated by Django 3.1.4 on 2021-02-12 20:36

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20210212_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageinfo',
            name='cropping',
        ),
        migrations.AddField(
            model_name='article',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('img_description', '450x350', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AddField(
            model_name='banner',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('banner', '1400x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
