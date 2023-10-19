from django.db import models

class Tag (models.Model):
    name =  models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text= 'A label for URL Config')

    def __str__ (self):
        return self.name
    class Meta:
        ordering = ['name']




class Startup (models.Model):
    name =models.CharField(max_length=21, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text= 'A label for URL Config.')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField()

    def __str__ (self):
        return self.name

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'


class Newslink (models.Model):
    title = models.CharField()
    pub_date = models.DateField('date published')
    link = models.URLField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag)
    def __str__ (self):
        return f"{self.startup}, {self.title}"    
    


    class Meta:
        verbose_name = 'news article'
        ordering = ['title']
        get_latest_by = 'pub_date'
# Create your models here.
