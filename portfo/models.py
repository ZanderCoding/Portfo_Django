from django.db import models

# Create your models here.


class Skill(models.Model):

    FIELD = (
        ("web development", "Web Development"),
        ("automation", "Automation"),
        ("artifiacl intelligence", "Artifiacl Intelligence"),
        ("cyber security", "Cyber Security"),
    )

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    field = models.CharField(
        max_length=100, choices=FIELD, blank=True, null=True)
    langsymbol = models.ImageField(
        upload_to='lang_symbol', blank=True, null=True)
    cert = models.ImageField(upload_to='certs', blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.field}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    source_code = models.URLField(blank=True, null=True)
    frameworks = models.TextField(max_length=200, blank=True, null=True)
    features = models.CharField(max_length=200, blank=True, null=True)
    installation = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
