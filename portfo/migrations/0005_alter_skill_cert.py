# Generated by Django 4.2.7 on 2023-11-28 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0004_rename_projects_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='cert',
            field=models.FileField(blank=True, null=True, upload_to='certs'),
        ),
    ]
