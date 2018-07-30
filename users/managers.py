from django.db import models
from django.contrib.auth.models import BaseUserManager

from django.utils import timezone


class UserManager(BaseUserManager):
    """UserManager provides helper methods to query User model."""

    def get_teachers(self):
        # return users who are teachers, which will be used for courses' detail.
        qs = super().get_queryset().filter(is_teacher=True)
        return qs

    def get_students(self):
        # return users, who are not teachers, are students.
        qs = super().get_queryset().filter(is_teacher=False)
        return qs

    def _create_user(self, email, password, is_staff, is_superuser,
                     **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)
