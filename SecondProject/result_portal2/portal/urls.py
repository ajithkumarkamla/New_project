from django.urls import path
from . import views

app_name = "portal"

urlpatterns = [
    # login & result
    
    path("",        views.login_view,  name="login"),
    path("home/",   views.result_view, name="result"),

    # jam dashboard
    path("jam/",    views.jam_dashboard, name="jam_dashboard"),

    # Student CRUD
    path("students/",                views.StudentList.as_view(),   name="student_list"),
    path("students/add/",            views.StudentCreate.as_view(), name="student_add"),
    path("students/<int:pk>/edit/",  views.StudentUpdate.as_view(), name="student_edit"),
    path("students/<int:pk>/delete/",views.StudentDelete.as_view(), name="student_delete"),

    # Result CRUD
    path("results/",                 views.ResultList.as_view(),    name="result_list"),
    path("results/add/",             views.ResultCreate.as_view(),  name="result_add"),
    path("results/<int:pk>/edit/",   views.ResultUpdate.as_view(),  name="result_edit"),
    path("results/<int:pk>/delete/", views.ResultDelete.as_view(),  name="result_delete"),
]
