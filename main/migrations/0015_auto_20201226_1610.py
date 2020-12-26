# Generated by Django 3.1.4 on 2020-12-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201223_1325'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobAvailable',
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Môn học', 'verbose_name_plural': 'Môn học'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'Trường', 'verbose_name_plural': 'Trường'},
        ),
        migrations.AlterField(
            model_name='level',
            name='levelName',
            field=models.CharField(choices=[('DH', 'Đại học'), ('SDH', 'Sau đại học'), ('TS', 'Thạc sĩ')], max_length=200, null=True),
        ),
    ]
