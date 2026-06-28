from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    price = models.DecimalField(max_digits=8, decimal_places=3)


    def __str__(self):
        return self.name