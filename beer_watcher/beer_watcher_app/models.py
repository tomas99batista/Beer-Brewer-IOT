from django.db import models

# Create your models here.
class BeerValues(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    temperature = models.FloatField(null=False)
    humidity = models.FloatField(null=False)

    def __str__(self) -> str:
        return f"{self.id} | {self.timestamp}: T {self.temperature} | H {self.humidity}"