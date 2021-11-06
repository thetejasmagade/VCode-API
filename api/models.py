from django.db import models

# Create your models here.


class UserData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name


class Code(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    codetitle = models.CharField(max_length=255)
    codedescription = models.CharField(max_length=555, blank=True)
    htmlcode = models.TextField(max_length=None, blank=True)
    jscode = models.TextField(max_length=None, blank=True)

    def __str__(self):
        return self.name
