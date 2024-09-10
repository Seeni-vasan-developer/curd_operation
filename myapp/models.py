from django.db import models

class StudentDetails(models.Model):
    student_name = models.CharField(max_length=50,null=True,blank=True)
    student_age = models.IntegerField()
    student_location = models.CharField(max_length=100,null=True)
    

