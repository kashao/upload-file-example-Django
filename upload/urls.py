from django.urls import path
from . import views

app_name = 'upload'

urlpatterns = [
    path('upload_file/', views.upload_file, name='upload_file'),
]