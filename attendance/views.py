from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView
from django.http import HttpResponse

from django.contrib.auth import get_user_model
# Create your views here.
class FrontPageView(TemplateView):
    template_name = 'front_page.html'


class FindStudentView(View):

    def get(self, request):
        student_id = request.GET['student_id']
        student = get_object_or_404(get_user_model(), as_id=student_id)
        html = '<html>' + student.english_name + '</html>'
        return HttpResponse(html)

        
