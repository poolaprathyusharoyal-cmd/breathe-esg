from django.db import models

class EmissionRecord(models.Model):
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    unit = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.source
