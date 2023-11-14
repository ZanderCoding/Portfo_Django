from django.db import models

# Create your models here.
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
