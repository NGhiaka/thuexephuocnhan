from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
# from django_ajax.decorators import ajax
# Create your views here.
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from carservice.forms import *
from carservice.models import *
from django.views.generic import ListView, TemplateView
# from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import F, Q, Sum
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
import json
# from passlib.hash import pbkdf2_sha256

# class indexList(ListView):
#     template_name = 'carservice/page/index.html'
#     model  = Schedule




def index(request):
    expense = Expense.objects.values('type_cost', 'date_enxpense__year', 'date_enxpense__month').annotate(cost=Sum('cost')).order_by('date_enxpense__year', 'date_enxpense__month')

    # today = datetime.today()
    # schs = Schedule.objects.all()
    # forms = []
    # schedule = Schedule.objects.filter(departure_day__lte = today, destination_day__gte = today)
    # context = {}
    # for sch in schs:
    #     # form = ScheduleForm(instance = sch)
    #     forms.append({'title':sch.customer,'start':sch.departure_day.strftime('%Y-%m-%d'),'end': sch.destination_day.strftime('%Y-%m-%d')})
    #     context = {
    #         'schedules':schedule, 
    #         'forms': forms,
    #         'user':request.user,
    #         'expenses': expense
    #     }

    return render(request, 'carservice/dashboard/index.html', {'expenses': expense})

def load_schedule(request):
    first_day  = datetime.today().replace(day=1)
    schedules = Schedule.objects.filter(Q(departure_day__gte=first_day) | Q(destination_day__gte=first_day))
    # data = [{
    #  "s":1
    # }, {"s":2}]
    data = list()
    for sch in schedules:
        obj = {
            'title': sch.car.nameofcar + " ("+sch.car.carid+") " +" - "+ sch.customer.name + "("+sch.customer.phone+")",
            'start': str(sch.departure_day),
            'end': str(sch.destination_day),
        }
        data.append(obj)
    return JsonResponse(json.dumps(data), content_type="application/json", safe=False)

def report(request):
    exps = Expense.objects.values('type_cost', 'date_enxpense__year', 'date_enxpense__month').annotate(cost=Sum('cost')).order_by('date_enxpense__year', 'date_enxpense__month')
    data = list()
    for exp in exps:
        obj = {
            'type': exp.type_cost,
            'cost': exp.cost,
            'time': exp.date_enxpense__month + '/' + exp.date_enxpense__year,
        }
        data.append(obj)
    return JsonResponse(json.dumps(data), content_type="application/json", safe=False)
def service(request):
    return render(request, 'carservice/page/service.html')

def statistical_income(request):
    return render(request, 'carservice/page/statistical_income.html')



# def schedule_json(request):
#     data_list = []
#     data_json = {}
#     # if request.is_ajax():
#     #     if request.method == 'POST':
#     schedule_list = Schedule.objects.all()        
#     if schedule_list:
#         for sch in schedule_list:
#             data = {
#                 'date': sch.departure_day,
#                 "badge":True,
#                 "title":"Tonight",
#                 'body': sch.guess_name,
#                 "footer":"At Paisley Park",
#                 "classname":"purple-event"
#             }
#             data_list.append(data)

#     data_json['key'] = data_list
#     # d = serializers.serialize('json', data_json)

    # return data_list
    # return JsonResponse(data_list, safe=False)  #

def login(request):
    if request.user.is_authenticated:
        return redirect('/admin')
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['fullname']:
                error_message = 'Vui lòng nhập họ tên!!'
            elif User.objects.filter(username=form.cleaned_data['username']).exists():
                error_message = 'Tài khoản đã được tạo'
            elif form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                error_message = 'Mật khẩu nhập lại không khớp!!!'
            else:
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('admin/')
    registerForm = UserRegisterForm() 
    return render(request, 'carservice/login/signup.html', {'form': registerForm, 'error_message': error_message})

def handler404(request):
    return render(request, 'carservice/page/404.html', status=404)

def handler500(request):
    return render(request, 'carservice/page/500.html', status=500)
    