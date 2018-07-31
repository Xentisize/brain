from django.urls import path

from .views import FrontPageView, FindStudentView

app_name = 'attendance'
urlpatterns = [
    path('', FrontPageView.as_view(), name='front_page'),
    path('find_student/', FindStudentView.as_view(), name='find_student'),
]