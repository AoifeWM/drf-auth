from django.contrib.auth import get_user_model
from django.db import models


class Sale(models.Model):
    name = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price_each = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " x " + str(self.quantity)

