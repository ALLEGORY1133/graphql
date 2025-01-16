from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,max_length=255,related_name='authors',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
