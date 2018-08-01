from django.contrib import admin

from .models import Weekday, DailySchedule


admin.site.register(Weekday)
admin.site.register(DailySchedule)
