from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,default="Категория")
 
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50,default="Название")
    prev_img = models.ImageField(upload_to='articles_img')
    subtitle = models.CharField(max_length=50,default="Подзаголовок")
    authors = models.CharField(max_length=50,default="Участники создания статьи")
    edit_data = models.DateTimeField(auto_now=True)
    pub_data = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    content = RichTextField(default="Текст статьи")
    publish = models.BooleanField(default = False)
    def __str__(self):
        return self.title
        