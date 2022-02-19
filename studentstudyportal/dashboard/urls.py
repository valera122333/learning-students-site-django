from django.urls import URLPattern, path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes')
]
