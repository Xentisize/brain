from django import forms
from django.contrib.auth import get_user_model

from scheduler.models import Weekday
from courses.models import Course


class CreateCourseForm(forms.ModelForm):
    student = forms.ModelMultipleChoiceField(queryset=get_user_model().roles.get_students())
    teacher = forms.ModelChoiceField(queryset=get_user_model().roles.get_teachers())

    class Meta:
        model = Course
        fields = ['title', 'subject', 'student', 'teacher', 'duration', 'time', 'price', 'weekday_for_lessons', 'active']
