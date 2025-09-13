# student/urls.py
from django.urls import path
from .views import StudentListCreate, StudentDetail

urlpatterns = [
    path('students/', StudentListCreate.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
]
