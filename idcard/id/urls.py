from django.urls import path
from .views import index, IdView, generate


urlpatterns = [ 
    path('', index, name='index'),
    path('<slug:slug>/', IdView.as_view(), name='idcard'), 
    path('generate/<roll>/', generate, name='generate'),
    ]
