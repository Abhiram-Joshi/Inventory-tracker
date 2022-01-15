from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    seller = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Shipment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_shipped = models.DateField(auto_now_add=True)
    cancelled = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name