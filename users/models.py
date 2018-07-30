from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    """This is the user model in our matrix. Each user shall have its personal information and role. User can be differentiated by their roles in teachers and students."""

    roles = UserManager()

    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    GRADE = (
        (0, 'Pre-Sch'), (1, 'K1'), (2, 'K2'), (3, 'K3'), (4, 'P1'), (5, 'P2'), (6, 'P3'), (7, 'P4'), (8, 'P5'), (9, 'P6'), (10, 'S1'), (11, 'S2'), (12, 'S3'), (13, 'S4'), (14, 'S5'), (15, 'S6'), (16, 'Uni'), (17, 'Others'),
    )

    # Basic personal information
    as_id = models.CharField("AS ID", max_length=20, unique=True, db_index=True)
    is_teacher = models.BooleanField(default=False)

    # active = models.BooleanField(default=True) # active is built-in
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50, blank=True)
    chinese_name = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='F')
    birthday = models.DateField(blank=True, null=True)

    # Contact information
    home_tel = models.CharField(max_length=20, blank=True, null=True)
    mobile_tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)


    # School Information
    school = models.ForeignKey('School', on_delete=models.CASCADE, blank=True, null=True)
    grade = models.SmallIntegerField(choices=GRADE, default=17)

    # Parental/Gudiance Information
    guidance = models.ForeignKey('Guidance', on_delete=models.CASCADE, blank=True, null=True)

    # Entry Information
    referral = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    entry_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """Return the english name with full name for object instance."""
        return f'{self.english_name} {self.last_name} ({self.first_name})'

    class Meta:
        ordering = ('english_name', 'last_name')

    
class School(models.Model):
    """School represents the information of a user's school."""
    english = models.CharField(max_length=200)
    chinese = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    def __str__(self):
        """Return the english name of the school for a school instance."""
        return f'{self.english}'
    
    class Meta:
        ordering = ('english', )


class Guidance(models.Model):
    """Guidance represents the emergency contact person for a student."""
    
    MOM = 0
    DAD = 1
    RELATIVES = 2
    FRIENDS = 3
    OTHER = 4

    RELATIONSHIP = (
        (MOM, 'Mother'), (DAD, 'Father'), (RELATIVES, 'Relatives'), (FRIENDS, 'Friends'), (OTHER, 'Other')
    )

    name = models.CharField(max_length=100, blank=True, null=True)
    relationship = models.SmallIntegerField(choices=RELATIONSHIP, default=OTHER)
    contact = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.contact})'
