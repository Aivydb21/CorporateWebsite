# Generated by Django 4.1.4 on 2023-01-11 11:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MissionPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_banner', models.ImageField(upload_to='mission_banner/images')),
                ('banner_title', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('title_description', ckeditor.fields.RichTextField()),
                ('mission_main_title', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='mission/images')),
            ],
            options={
                'verbose_name_plural': 'Mission',
            },
        ),
    ]
