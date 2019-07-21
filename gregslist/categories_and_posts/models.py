from django.conf import settings
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.CharField(max_length=200) 
    
    def __str__(self):
        return f"id={self.id}, category_name={self.category_name}, category_description={self.category_description}"


class Post(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    
    def __str__(self):
        return f"id={self.id}, title={self.title}, content={self.content}"