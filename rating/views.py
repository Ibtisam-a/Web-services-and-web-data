from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from math import ceil
# Create your views here.
def index(request):
    return HttpResponse("undefined URL")

def list(request):
    username = request.GET['username']
    if(Student.objects.get(username = username).logged_in):
        Courses = Course.objects.all()
        formatted_string = ''
        for course in Courses:
            formatted_string += f'{course.code}   {course.title}     {course.year}     {course.semester}     {course.teacher.name}\n'
        return HttpResponse(formatted_string)
    else:
        return HttpResponse("Not Authenticated")


def ratinglist(request):
    username = request.GET['username']
    if(Student.objects.get(username = username).logged_in):
        Teachers = Teacher.objects.all()
        formatted_string = ''
        for teacher in Teachers:
            ratings = Rating.objects.filter(teacher = teacher)
            for rating in ratings:
                total = rating.value
            total_rating =  ceil(total/ratings.count()) if ratings.count() > 0 else 0
            status = "Excellent" if total_rating > 3 else ( "Good" if total_rating > 1  else "Poor")
            stars = total_rating * '*'
            formatted_string += f'The rating of professor {teacher.name}: {status} - {stars} \n'

        return HttpResponse(formatted_string)
    else:
        return HttpResponse("Not Authenticated");

def rating(request):
    username = request.GET['username']
    teacher = request.GET['teacher']
    course = request.GET['course']
    if(Student.objects.get(username = username).logged_in):
        this_teacher = Teacher.objects.get(name = teacher)
        this_course = Course.objects.get(code = course)
        ratings = Rating.objects.filter(teacher = this_teacher, course=this_course)
        for rating in ratings:
            total = rating.value
        total_rating =  ceil(total/ratings.count()) if ratings.count() > 0 else 0
        status = "Excellent" if total_rating > 3 else ( "Good" if total_rating > 1  else "Poor")
        stars = total_rating* '*'
        formatted_string = f'The rating of professor {this_teacher.name} for module {this_course.title}: {status} - {stars} \n'
        return HttpResponse(formatted_string)
    else:
        return HttpResponse("Not Authenticated");


def rate(request):
    username = request.GET['username']
    teacher = request.GET['teacher']
    course = request.GET['course']
    rating = request.GET['rating']
    if(Student.objects.get(username = username).logged_in):
        if (int(rating) > 5) or (int(rating) < 0) :
            return HttpResponse("Invalid Rating provided");
        #try:
        this_teacher = Teacher.objects.get(name = teacher)
        this_course = Course.objects.filter(code = course).first()
        #except:
            #return HttpResponse("one or more invalid inputs")
        instance = Rating.objects.create(value=rating, teacher=this_teacher, course=this_course)
        return HttpResponse("Successfully Rated");
    else:
        return HttpResponse("Not Authenticated");

def register(request):
    username = request.GET['username']
    email = request.GET['email']
    password = request.GET['password']

    if(Student.objects.filter(username = username).count()==0):
        instance = Student(username=username, email=email, password=password)
        instance.save()
        return HttpResponse("successfully registered")
    else:
        return HttpResponse("User Already Resigtered")

def login(request):
    username = request.GET['username']
    password = request.GET['password']
    if(Student.objects.filter(username = username, password = password).count()>0):
        stud = Student.objects.get(username = username, password = password)
        if(not stud.logged_in):
            instance = Student.objects.update(username = username, logged_in= True)
            user = Student.objects.get(username = username)
            formatted_string = f'successfully logged in :{user.username}'
            return HttpResponse(formatted_string)
        else:
            return HttpResponse("Already Logged in")
    else:
        return HttpResponse("User not found.")

def logout(request, username):
    if(Student.objects.get(username = username)):
        stud = Student.objects.get(username = username)
        if(stud.logged_in):
            instance = Student.objects.update(username = username, logged_in= False)
            return HttpResponse("successfully logged out")
        else:
            return HttpResponse("Already Logged out")
    else:
        return HttpResponse("User not found.")
