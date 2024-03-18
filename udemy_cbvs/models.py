from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=256,null=True)
    principal=models.CharField(max_length=256,null=True)
    location=models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("udemy_cbvs:detail", kwargs={"pk": self.pk})
    

class Student(models.Model):
    name=models.CharField(max_length=256)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    