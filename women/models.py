from django.db import models
from django.urls import reverse
from .models import *

class Women(models.Model):
    title = models.CharField(max_length=255) #CharField для вставления текста с указанием макс кол символов например 255 
    content = models.TextField(blank=True) #TextField 
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True) # устанавливает время. не меняет время
    time_update = models.DateTimeField(auto_now=True) # устанавливает время. может менять время
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})