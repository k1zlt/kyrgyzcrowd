from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/images/')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
@receiver(pre_save, sender=Project)
def pre_save_slug(sender, **kwargs):
    slug = slug2 = slugify(kwargs['instance'].title)
    counter = 0
    while Project.objects.filter(slug=slug2).exists():
        slug2 = slug + '-' + str(counter)
        counter += 1
    kwargs['instance'].slug = slug2
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name