from django.contrib import admin
from .models import Teacher, Course, Rating, Student
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Rating)
admin.site.register(Student)
