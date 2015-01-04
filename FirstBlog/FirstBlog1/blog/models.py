from django.db import models
from django import forms

# Create your models here.

class posts(models.Model):

    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

class dataform(forms.Form):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=30)
    school = forms.CharField(max_length=100)

