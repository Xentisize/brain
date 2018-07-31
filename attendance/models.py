from django.db import models

from courses.models import Course
from django.contrib.auth import get_user_model


class Lesson(models.Model):
    """Lesson represents a single lesson which will include the course and attendance."""
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    datetime = models.DateTimeField()


class Entry(models.Model):
    """Entry instance is a single attendance record for a lesson."""
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    enter = models.DateTimeField(auto_now_add=True)
    leave = models.DateTimeField(blank=True)
    manual = models.BooleanField(default=False)
    
    duration = models.DurationField(blank=True)

    def __str__(self):
        return f'{self.lesson} ({self.enter})'


