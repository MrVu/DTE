# Generated by Django 3.1.4 on 2020-12-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20201228_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, null=True)),
                ('guest_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('ielts_overall', models.FloatField(choices=[('', 'IELTS trung bình'), (4, '4.0'), (4.5, '4.5'), (5, '5.0'), (5.5, '5.5'), (6, '6.0'), (6.5, '6.5'), (7, '7.0')], null=True)),
                ('ielts_min', models.FloatField(choices=[('', 'IELTS thấp nhất'), (4, '4.0'), (4.5, '4.5'), (5, '5.0'), (5.5, '5.5'), (6, '6.0'), (6.5, '6.5'), (7, '7.0')], null=True)),
                ('level', models.CharField(choices=[('Đại học', 'Đại học'), ('Sau đại học', 'Sau đại học'), ('Thạc sĩ', 'Thạc sĩ')], max_length=200, null=True)),
            ],
        ),
    ]
