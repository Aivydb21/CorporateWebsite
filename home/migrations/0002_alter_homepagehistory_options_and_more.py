# Generated by Django 4.1.4 on 2023-01-04 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepagehistory',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.RenameField(
            model_name='homepagecontent',
            old_name='services_title_gradient_text',
            new_name='services_title',
        ),
        migrations.RenameField(
            model_name='homepagehistory',
            old_name='gradient_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='services_title_simple_text',
        ),
        migrations.RemoveField(
            model_name='homepagehistory',
            name='simple_title',
        ),
        migrations.DeleteModel(
            name='HomePageServices',
        ),
    ]
