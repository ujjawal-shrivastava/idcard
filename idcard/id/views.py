from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import Student

from django.http import HttpResponse
import requests

def index(request):

    if request.method == 'POST':
        roll_no = request.POST.get("roll_no", "")
        redirect_url = '/'+str(roll_no)
        return redirect(redirect_url)

    
    else:
        return render(request, 'index.html')



class IdView(DetailView):
    model = Student
    slug_field = 'roll'
    template_name = 'id_card.html'

def generate(request, roll):
    obj = Student.objects.get(roll=roll)
    filename = 'ID-Card '+obj.name+' ('+str(obj.roll)+')'
    api_url = 'https://script.google.com/macros/s/AKfycbyKIQ7weX-Zd_xkBI2o0XI5rv1Tsa0okzlTngZMNp5-tT_7KCYU/exec?name='+obj.name
    response = requests.get(api_url)
    response = HttpResponse(requests.get(response.content))
    response['content_type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment;filename={0}.pdf'.format(filename)
    return response

