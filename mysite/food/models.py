from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="media/", blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name