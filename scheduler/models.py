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

    def __str__(self):
        return f'{Weekday.WEEKDAYS[self.day-1][1]}'
