from django.db import models

# Create your models here.


class customer(models.Model):
    name = models.CharField(max_length=50)
    fm_number = models.CharField(max_length=15,unique=True)
    shirt_height = models.CharField(max_length=50)
    shirt_width = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    

class order(models.Model):
    customerFK = models.ForeignKey(customer,on_delete=models.CASCADE)
    numberofsuits = models.PositiveSmallIntegerField()
    date_ordered = models.DateField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    modified = models.DateTimeField (auto_now=True)
