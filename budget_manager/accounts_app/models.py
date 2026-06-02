from django.db import models
from datetime import date

# Create your models here.
class Account(models.Model):
    sl_no = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.category} - ₹{self.amount}"