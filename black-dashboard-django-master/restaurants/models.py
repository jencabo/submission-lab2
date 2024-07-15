from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    opening_hours = models.TimeField()
    phone_number = models.CharField(max_length=15)
    rating = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    owner_email = models.EmailField(unique=False, null=True, blank=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
