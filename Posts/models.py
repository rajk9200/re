from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
class PostCot(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# Create your models here.
from ckeditor.fields import RichTextField
class Posts(models.Model):
    title = models.ForeignKey(PostCot, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_date =models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    sort_info = models.TextField()
    desc = RichTextField()
    slug =models.SlugField(default="-")
    active = models.BooleanField(default=True)
    # email = models.EmailField(unique=True)

    # def __str__(self):
    #     return self.name

import random
def update_slug(sender,instance,**kwargs):
    path =str(instance.name).replace(" ","-")+str(random.randrange(11,5555))
    instance.slug=path



pre_save.connect(update_slug,sender=Posts)

class ResultLink(models.Model):
    link_text = models.CharField(max_length=200)
    link_tag = models.CharField(max_length=100)

    def __str__(self):
        return self.link_text


