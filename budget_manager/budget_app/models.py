from django.db import models


# Create your models here.
class Budget(models.Model):
    sl_no = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.category}: {self.amount}"