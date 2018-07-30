from django.db import models
from django.contrib.auth import get_user_model

import datetime


class Course(models.Model):
    """Course represents a single lesson for a student."""

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    WEEKDAYS = ((MONDAY, 'Monday'), (TUESDAY, 'Tuesday'), (WEDNESDAY, 'Wednesday'), (THURSDAY, 'Thursday'), (FRIDAY, 'Friday'), (SATURDAY, 'Saturday'), (SUNDAY, 'Sunday'))

    # Constant for setting the default lesson duration.
    DEFAULT_LESSON_DURATION = datetime.timedelta(hours=1)

    SUBJECTS = (('Chinese', 'Chinese'), ('English', 'English'), ('Mathematics', 'Mathematics'), ('Liberal Studies', 'Liberal Studies'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Economics', 'Economy'), ('Japanese', 'Japanese'), ('Examinations', 'Examinations'), ('Other', 'Other'))

    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50, choices=SUBJECTS)
    student = models.ForeignKey(get_user_model(), related_name='students', on_delete=models.CASCADE)
    teacher = models.ForeignKey(get_user_model(), related_name='teachers', on_delete=models.CASCADE)
    # Duration is the length of the lesson
    duration = models.DurationField(default=DEFAULT_LESSON_DURATION, help_text='Format: [HH:MM:SS]')
    time = models.TimeField(help_text='Format: [HH:MM:SS]')
    weekday_for_lessons = models.SmallIntegerField(choices=WEEKDAYS)
    # lessons_per_week can be deduced from weekdays 
    # lessons_per_week = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.title} ({self.student.english_name} {self.student.last_name})'