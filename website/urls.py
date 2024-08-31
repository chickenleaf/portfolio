from django.urls import path
from . import views
from django.contrib import admin

# Django Admin header customization
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to Portfolio Portal"

urlpatterns = [
    path('', views.landing, name='landing'),
    path('landing.html', views.contact_view, name='contact'),
    path('download-resume/', views.download_resume, name='download_resume'),
]
