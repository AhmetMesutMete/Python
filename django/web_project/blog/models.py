from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}'


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name