from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('get-result/', views.get_result, name='get_result'),
]