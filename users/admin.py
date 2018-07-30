from django.contrib import admin

from .models import User, Guidance, School
# Register your models here.

class UserAdmin(admin.ModelAdmin):

    list_display = ('english_name', 'last_name', 'first_name', 'mobile_tel', 'guidance')
    search_fields = ('english_name', )
    autocomplete_fields = ('school', )


admin.site.register(User, UserAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('district', 'english', 'chinese', )
    search_fields = ('english', 'district')
    list_filter = ('district', )


admin.site.register(School, SchoolAdmin)
admin.site.register(Guidance)
