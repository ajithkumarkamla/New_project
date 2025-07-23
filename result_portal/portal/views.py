import random
import datetime
from django.shortcuts import render, redirect
from django.core.cache import cache
from .forms   import LoginForm
from .models  import Student, Result


def _simulate_stats():
    """
    Return a dict that mimics heavy‑traffic dashboard numbers.
    'users_trying' key auto‑expires every 10 s → keeps count realistic.
    """
    users = cache.get_or_set("users_trying", 0, timeout=10)
    cache.incr("users_trying")          # +1 for every request

    load = random.randint(15, 90)       # ← separate assignment (no walrus)

    return {
        "users_trying": users,
        "routed_to"   : f"Server {random.randint(1, 2)}",
        "server_load" : load,
        "status"      : "High Load" if load >= 50 else "Normal",
    }


def login_view(request):
    stats     = _simulate_stats()
    cache_hit = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            reg = form.cleaned_data["register_number"]
            dob = form.cleaned_data["dob"]

            # Try Redis / LocMem cache first
            key      = f"student:{reg}"
            student  = cache.get(key)
            cache_hit = bool(student)

            if not student:
                student = Student.objects.filter(
                    register_number=reg, dob=dob
                ).first()
                if student:
                    cache.set(key, student, timeout=60)

            if student:
                request.session["sid"] = student.id
                return redirect("portal:result")
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, "portal/login.html", {
        "form"      : form,
        "cache_hit" : cache_hit,
        **stats,
    })


def result_view(request):
    sid = request.session.get("sid")
    if not sid:
        return redirect("portal:login")

    student = Student.objects.get(id=sid)
    result  = Result.objects.filter(student=student).first()

    return render(request, "portal/result.html", {
        "student": student,
        "result" : result,
        "now"    : datetime.datetime.now(),
    })
