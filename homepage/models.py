from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class HomePage(models.Model):
    title = models.CharField(max_length=150)
    welcome = RichTextField(default='')
    about = RichTextField(default='')
    services = RichTextField(blank=True)
    portfolio = RichTextUploadingField(default='')
    contact = RichTextField(default='')
