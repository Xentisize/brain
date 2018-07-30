from django.contrib import admin
from django import forms

from .models import User, Guidance, School
# Register your models here.

class GudianceInline(admin.StackedInline):
    # contact = forms.IntegerField(widget=forms.TextInput)
    model = Guidance
    extra = 1


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'english_name', 'last_name', 'first_name', 'mobile_tel', )
    inlines = [ GudianceInline, ]
    search_fields = ('english_name', )
    autocomplete_fields = ('school', )
    list_filter = ('is_teacher', )


admin.site.register(User, UserAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('district', 'english', 'chinese', )
    search_fields = ('english', 'district')
    list_filter = ('district', )


admin.site.register(School, SchoolAdmin)
admin.site.register(Guidance)
