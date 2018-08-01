from django.db import models
from django.contrib.auth import get_user_model

import datetime

from scheduler.models import Weekday
from .managers import CourseManager


class Course(models.Model):
    """Course represents a single lesson for a student."""

    courses_list = CourseManager()

    # Constant for setting the default lesson duration.
    DEFAULT_LESSON_DURATION = datetime.timedelta(hours=1)

    SUBJECTS = (('Chinese', 'Chinese'), ('English', 'English'), ('Mathematics', 'Mathematics'), ('Liberal Studies', 'Liberal Studies'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Economics', 'Economics'), ('Japanese', 'Japanese'), ('Examinations', 'Examinations'), ('Other', 'Other'))

    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50, choices=SUBJECTS)
    students = models.ManyToManyField(get_user_model(), related_name='courses')
    teacher = models.ForeignKey(get_user_model(), related_name='teaching_courses', on_delete=models.CASCADE)
    # Duration is the length of the lesson
    duration = models.DurationField(default=DEFAULT_LESSON_DURATION, help_text='Format: [HH:MM:SS]')
    time = models.TimeField(help_text='Format: [HH:MM:SS]')
    # weekday_for_lessons: SmallIntergerField can't fit into the database for multi-selection.
    weekday_for_lessons = models.ManyToManyField(Weekday)
    # lessons_per_week can be deduced from weekdays 
    # lessons_per_week = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        english_names = ', '.join(sorted([student.english_name for student in self.students.all()]))
        return f'{self.title} ({english_names})'