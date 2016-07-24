from __future__ import unicode_literals

from django.db import models


# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField("images")
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    comment = models.TextField()
    submission_date = models.DateTimeField(auto_now=True)
