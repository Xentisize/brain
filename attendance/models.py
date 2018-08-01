from django.db import models
from django.contrib.auth import get_user_model


class Entry(models.Model):
    """Entry instance is a single attendance record for a lesson."""
    # lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    enter = models.DateTimeField(blank=True, null=True)
    leave = models.DateTimeField(blank=True, null=True)
    manual = models.BooleanField(default=False)
    
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f'Entry - {self.pk} ({self.enter})'


class Lesson(models.Model):
    """Lesson represents a single lesson which will include the course and attendance."""

    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    record = models.OneToOneField('attendance.Entry', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course.title} - {self.student.english_name} ({self.datetime})'
