import random, datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.cache import cache
from django.http import JsonResponse
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from .forms  import LoginForm, StudentForm, ResultForm
from .models import Student, Result

# ---------- traffic‑sim helper ----------
def _simulate_stats():
    users = cache.get_or_set("users_trying", 0, timeout=10)
    cache.incr("users_trying")
    load = random.randint(15, 90)
    return {
        "users_trying": users,
        "routed_to"   : f"Server {random.randint(1, 2)}",
        "server_load" : load,
        "status"      : "High Load" if load >= 50 else "Normal",
    }

# ---------- login & result ----------
def login_view(request):
    stats, cache_hit = _simulate_stats(), None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            reg, dob = form.cleaned_data["register_number"], form.cleaned_data["dob"]
            key      = f"student:{reg}"
            student  = cache.get(key)
            cache_hit = bool(student)
            if not student:
                student = Student.objects.filter(register_number=reg, dob=dob).first()
                if student:
                    cache.set(key, student, timeout=60)
            if student:
                request.session["sid"] = student.id
                return redirect("portal:result")
            form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, "portal/login.html",
                  {"form": form, "cache_hit": cache_hit, **stats})

def result_view(request):
    sid = request.session.get("sid")
    if not sid:
        return redirect("portal:login")
    student = Student.objects.get(id=sid)
    result  = Result.objects.filter(student=student).first()
    return render(request, "portal/result.html",
                  {"student": student, "result": result,
                   "now": datetime.datetime.now()})

# ---------- jam dashboard ----------
def jam_dashboard(request):
    stats = _simulate_stats()
    if request.GET.get("ajax"):
        return JsonResponse(stats)
    return render(request, "portal/jam_dashboard.html", stats)

# ---------- Student CRUD ----------
class StudentList(ListView):
    model, template_name, paginate_by = Student, "portal/student_list.html", 20

class StudentCreate(CreateView):
    model, form_class, template_name = Student, StudentForm, "portal/student_form.html"
    success_url = reverse_lazy("portal:student_list")

class StudentUpdate(UpdateView):
    model, form_class, template_name = Student, StudentForm, "portal/student_form.html"
    success_url = reverse_lazy("portal:student_list")

class StudentDelete(DeleteView):
    model, template_name = Student, "portal/student_confirm_delete.html"
    success_url = reverse_lazy("portal:student_list")

# ---------- Result CRUD ----------
class ResultList(ListView):
    model, template_name, paginate_by = Result, "portal/result_list.html", 20

class ResultCreate(CreateView):
    model, form_class, template_name = Result, ResultForm, "portal/result_form.html"
    success_url = reverse_lazy("portal:result_list")

class ResultUpdate(UpdateView):
    model, form_class, template_name = Result, ResultForm, "portal/result_form.html"
    success_url = reverse_lazy("portal:result_list")

class ResultDelete(DeleteView):
    model, template_name = Result, "portal/result_confirm_delete.html"
    success_url = reverse_lazy("portal:result_list")
