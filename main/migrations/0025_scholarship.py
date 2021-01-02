# Generated by Django 3.1.4 on 2021-01-02 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20210102_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('value', models.IntegerField(null=True)),
                ('time', models.CharField(max_length=200)),
                ('uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.university')),
            ],
        ),
    ]
