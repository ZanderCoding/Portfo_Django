# Generated by Django 4.2.7 on 2023-11-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('source_code', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
