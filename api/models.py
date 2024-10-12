from django.db import models

# Create your models here.
class GoldRate(models.Model):
    rate = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.date}'
