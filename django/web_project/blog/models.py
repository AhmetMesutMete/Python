from django.db import models
from django.utils.text import slugify
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    description = models.TextField()
    '''
        At first I had some values inside of the table so first set
        the parameters in a way that accepts rows that doesn't have a value for
        slug field and migrate the changes
    '''
    # first value of null was True
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True, editable=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)