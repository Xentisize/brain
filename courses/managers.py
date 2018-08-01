from django.db.models import manager

from scheduler.models import Weekday
from django.contrib.auth import get_user_model


class CourseManager(manager.Manager):

    def get_courses_by_weekday(self, weekday):
        """Return the related courses for a weekday."""
        if weekday > 0 and weekday <= 7:
            weekday = Weekday.objects.get(day=weekday)
            courses = weekday.course_set.all()
            return courses

    def get_all_courses_by_week(self):
        """Return all courses on weekly basis. Depends on CourseManager#get_courses_by_weekday."""
        courses = []
        for i in range(1, 7):
            courses.append(self.get_courses_by_weekday(i))
        return courses

    def get_all_courses_by_student(self, student_pk):
        """Return all courses by a student."""
        student = get_user_model().roles.get_students().get(pk=student_pk)
        return student.courses.all()

    def get_all_courses_by_teacher(self, teacher_pk):
        """Return all teaching courses by a teacher."""
        teacher = get_user_model().roles.get_teachers().get(pk=teacher_pk)
        return teacher.teaching_courses.all()



