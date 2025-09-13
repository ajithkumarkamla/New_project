from django.urls import path
from .views import get_Emplooye,create_Emp

urlpatterns = [
    path('empusers/',get_Emplooye,name='get_Emplooye'),
    path('empusers/create/',create_Emp,name='create_Emp'),
]
