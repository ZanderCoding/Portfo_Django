# Generated by Django 4.2.7 on 2023-11-24 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0003_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]