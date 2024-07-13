from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# def index(request):
#     details = aboutpage.objects.all()
#     return render(request,'index.html',{'details1':details})


# def Hobbies(request):
#     Hobbies = Hobbies1.objects.all()
#     return render(request,'index.html',{'Hobbies':Hobbies})



def index(request):
    details = aboutpage.objects.all()
    Education_category = Education_category1.objects.all()
    Education_category_details = Education_category_details1.objects.all()
    skills = skills1.objects.all()
    Experience = Experience1.objects.all()
    context = {
        'details1': details,
        'Education_category' : Education_category,
        'Education_category_details' : Education_category_details,
        'skills_check' : skills,
        'Experience_check' : Experience
    }
    return render(request, 'index.html', context)
    