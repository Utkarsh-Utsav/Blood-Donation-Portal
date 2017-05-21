
from django.conf.urls import url, include
from . import views
from .models import Person
urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^donate/$',views.donate,name='donate'),
    url(r'^why_donate_blood/$', views.why_donate,name='why_donate')
]
