from django.contrib import admin

from .models import Course
from .forms import CreateCourseForm


class CourseAdmin(admin.ModelAdmin):
    form = CreateCourseForm
    

admin.site.register(Course, CourseAdmin)
