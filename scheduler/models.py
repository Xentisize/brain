from django.db import models


class Weekday(models.Model):
    """Weekday represents a weekday."""

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    WEEKDAYS = ((MONDAY, 'Monday'), (TUESDAY, 'Tuesday'),
                (WEDNESDAY, 'Wednesday'), (THURSDAY, 'Thursday'),
                (FRIDAY, 'Friday'), (SATURDAY, 'Saturday'), (SUNDAY, 'Sunday'))

    day = models.IntegerField(choices=WEEKDAYS)

    class Meta:
        ordering = ('day', )

    def __str__(self):
        return f'{Weekday.WEEKDAYS[self.day-1][1]}'


class DailySchedule(models.Model):
    """DailySchedule represents a schedule for a single day. It includes all the lesson in that day."""
    day = models.SmallIntegerField()
    weekday = models.ForeignKey('Weekday', on_delete=models.CASCADE)
    lesson = models.ForeignKey('attendance.Lesson', on_delete=models.CASCADE)

    class Meta:
        ordering = ("lesson__datetime", )

    def __str__(self):
        return f'{self.day} ({self.weekday})'


# class MonthlySchedule(models.Model):
#     """MonthlySchedule represents the whole schedule for a single month."""
#     year =