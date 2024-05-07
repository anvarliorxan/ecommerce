from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
