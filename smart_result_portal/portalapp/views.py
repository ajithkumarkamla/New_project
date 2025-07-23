from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import StudentResult
import random
from datetime import datetime

# Simulated global states
server_loads = [random.randint(10, 30), random.randint(30, 60), random.randint(20, 50)]
MAX_LOAD = 90
users_trying = 0

@csrf_exempt
def login_view(request):
    global server_loads, users_trying

    if request.method == 'POST':
        reg_no = request.POST.get('reg_no')
        dob = request.POST.get('dob')
        users_trying += 1

        redis_cache = {
            '22CSE001': 'Hit',
            '22CSE002': 'Hit',
        }

        redis_status = 'Hit' if reg_no in redis_cache else 'Miss'
        routed_server = server_loads.index(min(server_loads)) + 1
        server_loads[routed_server - 1] += 5
        current_load = server_loads[routed_server - 1]

        if current_load >= MAX_LOAD:
            server_status = "Server Down. Please Try Again Later."
        elif current_load > 75:
            server_status = "High Load"
        elif current_load > 40:
            server_status = "Medium Load"
        else:
            server_status = "Low Load"

        context = {
            'users_trying': users_trying,
            'redis_status': redis_status,
            'routed_server': routed_server,
            'server_load': current_load,
            'server_status': server_status,
        }

        return render(request, 'login.html', context)

    return render(request, 'login.html', {
        'users_trying': users_trying,
        'redis_status': '-',
        'routed_server': '-',
        'server_load': 0,
        'server_status': 'Waiting for Input',
    })


@csrf_exempt
def get_result(request):
    if request.method == 'POST':
        reg_no = request.POST.get('reg_no')
        dob = request.POST.get('dob')
        try:
            student = StudentResult.objects.get(register_number=reg_no, dob=dob)
            percentage = (student.total / 500) * 100
            return JsonResponse({
                'name': student.name,
                'subject1': student.subject1,
                'subject2': student.subject2,
                'subject3': student.subject3,
                'subject4': student.subject4,
                'subject5': student.subject5,
                'total': student.total,
                'percentage': round(percentage, 2),
            })
        except StudentResult.DoesNotExist:
            return JsonResponse({'error': 'No result found for provided credentials.'})
    return JsonResponse({'error': 'Invalid request.'})
