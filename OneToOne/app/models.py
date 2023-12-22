from django.db import models

# Create your models here.
class Capital(models.Model):
    Capital_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Capital_name

class Country(models.Model):
    Country_Name = models.CharField(max_length=100)
    Capital_name = models.OneToOneField(Capital,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Country_Name
    
class DEPT(models.Model):
    DEPT_Name = models.CharField(max_length=100)
    DEPT_No = models.IntegerField(primary_key=True)
    LOC = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.DEPT_Name
    
class EMP(models.Model):
    EMP_Id = models.IntegerField(primary_key=True)
    EMP_Name = models.CharField(max_length=100)
    DEPT_No = models.ForeignKey(DEPT,on_delete=models.CASCADE) 
    LOC = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.EMP_Name