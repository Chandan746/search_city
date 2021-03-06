# Generated by Django 3.1 on 2020-08-10 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tbapp', '0002_auto_20200811_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('className', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(blank=True, db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubSector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subSectors', models.CharField(db_index=True, max_length=50)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbapp.sector')),
            ],
        ),
    ]
