from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=500)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

