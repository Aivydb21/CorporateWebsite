# Generated by Django 4.1.4 on 2023-01-03 14:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('title_description', ckeditor.fields.RichTextField()),
                ('heading', models.CharField(max_length=100)),
                ('heading_description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='about/images')),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
    ]
