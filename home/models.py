from django.db import models


class ContactDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    me = models.TextField()