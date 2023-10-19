from django.db import models
from organizer.models import*

class Post(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique_for_month='pub_date', help_text= 'A label for URL Config.')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)

    tag = models.ManyToManyField(Tag, related_name='blog_posts')
    startup = models.ManyToManyField(Startup, related_name='blog_posts')

    def __str__ (self):
        return f"{self.title}, {self.pub_date('%Y-%m-%d')}"
    
    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'


# Create your models here.
