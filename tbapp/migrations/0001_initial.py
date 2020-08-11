# Generated by Django 3.1 on 2020-08-10 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('className', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('code', models.CharField(blank=True, max_length=5)),
                ('currency', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbapp.country')),
            ],
        ),
    ]
