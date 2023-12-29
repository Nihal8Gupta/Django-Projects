from django.db import models

# Create your models here.
class Course(models.Model):
    Cname = models.CharField(primary_key=True,max_length=100)
    Cfee = models.IntegerField()
    
    def __str__(self) -> str:
        return self.Cname

class Student(models.Model):
    Sid = models.IntegerField(primary_key=True)
    Sname = models.CharField(max_length=100)
    Sclass = models.CharField(max_length=100)
    Scourse = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Sname