from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length = 255)
    professor_id = models.CharField(max_length = 255, unique = True)

# Student user's model
class Student(models.Model):
    username = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 25)
    logged_in = models.BooleanField(default=False)


# Module's model
class Course(models.Model):
    code = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    year = models.IntegerField()
    semester = models.IntegerField()
    teachers = models.ManyToManyField('Teacher' , blank=True) #many to many relationship with teacher


#Ratings Model
class Rating(models.Model):
    value = models.FloatField()
    course = models.ForeignKey(Course , on_delete=models.CASCADE) #One to many with course
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE) #One to many with teacher
    students = models.ManyToManyField('student' , blank=True) #many to many relationship

    
