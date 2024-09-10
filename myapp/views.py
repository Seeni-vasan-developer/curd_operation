from django.shortcuts import render
from .models import *
from django.contrib import messages

def form_view(request):
    if request.method == "POST":
        student_name = request.POST['student_name']
        student_age = request.POST['student_age']
        student_location = request.POST['student_location']
        StudentDetails.objects.create(student_name=student_name, student_age=student_age,student_location=student_location)
        messages.success(request,"Details Stored Successfully")
        return render(request,'form_view.html')
    return render(request,'form_view.html')