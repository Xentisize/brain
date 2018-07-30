from django import forms
from django.contrib.auth import get_user_model

from .models import Course


class CreateCourseForm(forms.ModelForm):

    student = forms.ModelChoiceField(queryset=get_user_model().roles.get_students())
    teacher = forms.ModelChoiceField(queryset=get_user_model().roles.get_teachers())
    week_day_for_lessons = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Course.WEEKDAYS)

    class Meta:
        model = Course
        fields = ['title', 'subject', 'student', 'teacher', 'duration', 'time', 'price', 'week_day_for_lessons']
