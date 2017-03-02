from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#blue print for our database

class Company_table(models.Model):
    Company = models.CharField(max_length=128)
    Address = models.CharField(max_length=1024)
    #StartDate = models.DateField()
    CreditScore = models.IntegerField(4)
    Companylogo = models.CharField(max_length=1024,null=True)

    def __str__(self):
        return self.Company

class Loadboard_table(models.Model):
    Company = models.ForeignKey(Company_table, on_delete=models.CASCADE)
    Origin = models.CharField(max_length=128)
    Destination = models.CharField(max_length=128)
    Email = models.CharField(max_length=256)

    def __str__(self):
        return self.Origin + ' ---> ' + self.Destination

    def get_absolute_url(self):
        return reverse('loadboard:detail', kwargs={'pk': self.pk})


