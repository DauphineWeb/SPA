from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Quote(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    categories = models.ManyToManyField(Category, related_name='quotes')
    def __str__(self):
        return f"{self.content[:50]}... - {self.author.name}"
