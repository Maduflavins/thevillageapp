from django.db import models

# Create your models here.

class Plan(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    per = models.CharField(max_length=50,blank=True )
    benefit1 = models.CharField(max_length=50, blank=True)
    benefit2 = models.CharField(max_length=50, blank=True)
    benefit3 = models.CharField(max_length=50, blank=True) 
    benefit4 = models.CharField(max_length=50, blank=True)
    benefit5 = models.CharField(max_length=50, blank=True)
    benefit6 = models.CharField(max_length=50, blank=True)
    benefit7 = models.CharField(max_length=50, blank=True)
    benefit8 = models.CharField(max_length=50, blank=True)
    benefit9 = models.CharField(max_length=50, blank=True)
    benefit10 = models.CharField(max_length=50, blank=True)
    benefit11 = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.title
    





