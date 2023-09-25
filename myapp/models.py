from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=500)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.name

