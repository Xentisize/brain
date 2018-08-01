from django.db import models
from django.contrib.auth import get_user_model

# from courses.models import Course


class Lesson(models.Model):
    """Lesson represents a single lesson which will include the course and attendance."""
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    datetime = models.DateTimeField()


class Entry(models.Model):
    """Entry instance is a single attendance record for a lesson."""
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    enter = models.DateTimeField(blank=True)
    leave = models.DateTimeField(blank=True)
    manual = models.BooleanField(default=False)
    
    duration = models.DurationField(blank=True)

    def __str__(self):
        return f'{self.lesson} ({self.enter})'


