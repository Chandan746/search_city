from django.db import models

class Country(models.Model):
    id = models.CharField(unique=True,null=False, primary_key=True,max_length=50)
    className = models.CharField(max_length =20,null=False,blank=True)
    name = models.CharField(max_length =50,null=False,blank=True,db_index=True)
    code = models.CharField(max_length =5,null=False,blank=True)
    currency = models.CharField(max_length =50,null=False,blank=True)
    def __str__(self):
        return self.name    
class Cities(models.Model):
    city=models.CharField(max_length=50,null=False,blank=False,db_index=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.city    
class Sector(models.Model):
    id = models.CharField(unique=True,null=False, primary_key=True,max_length=50)
    className = models.CharField(max_length =20,null=False,blank=True)
    name = models.CharField(max_length =50,null=False,blank=True,db_index=True)
    def __str__(self):
        return self.name  
class SubSector(models.Model):
    subSectors = models.CharField(max_length=50,null=False,blank=False) 
    sector=models.ForeignKey(Sector,on_delete=models.CASCADE)
    def __str__(self):
        return self.subSectors  



