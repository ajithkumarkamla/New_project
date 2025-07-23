from django.urls import path
from .views import login_view, result_view

app_name = "portal"

urlpatterns = [
    path("",      login_view,  name="login"),
    path("home/", result_view, name="result"),
]
