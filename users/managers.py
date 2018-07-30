from django.db import models


class UserManager(models.Manager):
    """UserManager provides helper methods to query User model."""

    def get_teachers(self):
        # return users who are teachers, which will be used for courses' detail.
        qs = super().get_queryset().filter(is_teacher=True)
        return qs

    def get_students(self):
        # return users, who are not teachers, are students.
        qs = super().get_queryset().filter(is_teacher=False)
        return qs
