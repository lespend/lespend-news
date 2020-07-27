from django.db import models
from tinymce.models import HTMLField

class Article(models.Model):
    category_choices = (
        ('новости', 'новости'),
        ('обучение', 'обучение')
    )
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=100, choices=category_choices)
    text = HTMLField()
    publication_date = models.DateTimeField(auto_created=True)
    cover_image = models.ImageField(upload_to='media/', default='media/cardimage.jpg')

    def __str__(self):
        return f'{self.title} | {self.category.upper()}'
    

