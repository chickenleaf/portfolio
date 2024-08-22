from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('landing.html', views.contact_view, name='contact'),
]
