from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    rate = models.IntegerField()
    pages = models.IntegerField()
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='files/', null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MyUsers(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
