from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import *
from carservice.models import *
from django.contrib import messages
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# lich trinh



class CarList(ListView):
    template_name = 'carservice/schedule/carlist.html'
    model  = Car
    paginate_by = 20
    ordering = ['id']

class CustomerList(ListView):
    template_name = 'carservice/schedule/customerlist.html'
    model  = Customer

class ScheduleList(ListView):
    template_name = 'carservice/schedule/index.html'
    model  = Schedule


# def schedule(request):
#     schedule_list = Schedule.objects.all().values('id','name','company__name').order_by('-departure_day')
#     context = {
#         'schedule_list': schedule_list,
#     }
#     return render(request, 'carservice/schedule/index.html', context)

def schedule_new(request, car_id, customer_id):
    if request.method == 'POST': 
        f = ScheduleForm(request.POST)
        if f.is_valid(): 
            car = Car(id = car_id)
            customer = Customer(id=customer_id)
            sch = Schedule(
                car = car,
                customer = customer,
                departure_day = f.cleaned_data['departure_day'],
                destination_day = f.cleaned_data['destination_day'],
                departure = f.cleaned_data['departure'],
                destination = f.cleaned_data['destination'],
                departure_time = f.cleaned_data['departure_time'],
                price = f.cleaned_data['price'],
                deposit = f.cleaned_data['deposit'],
                status = f.cleaned_data['status'] 
                )
            od = sch.save()
        messages.success(request, "Thêm thành công!!!")
        return redirect('/admin/lich-trinh/chi-tiet/'+  str(car_id).strip())
    cF =  ScheduleForm()
    car = Car.objects.all()
    # cF.fields['car'].label_from_instance = lambda obj: "%s (%s)" % (c.name for c in car.nameofcar, c.name for c in car.carid)
    return render(request, 'carservice/schedule/new.html', {'form':cF})

def schedule_detail(request, car_id):
    try:
        schedule = Schedule.objects.get(id = car_id)
    except Schedule.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'carservice/schedule/show.html', {'schedule':schedule})
def schedule_edit(request, car_id):
    try:
        if request.method == 'POST': 
            f = ScheduleForm(request.POST)
            if f.is_valid(): 
                car = Schedule.objects.get(id=car_id)
                # car.car = f.cleaned_data['car']
                # car.guess_name = f.cleaned_data['guess_name']
                # car.email = f.cleaned_data['email']
                # car.phone_number = f.cleaned_data['phone_number']
                car.departure_day = f.cleaned_data['departure_day']
                car.destination_day = f.cleaned_data['destination_day']
                car.departure = f.cleaned_data['departure']
                car.destination = f.cleaned_data['destination']
                car.departure_time = f.cleaned_data['departure_time']
                car.price = f.cleaned_data['price']
                car.deposit = f.cleaned_data['deposit']
                car.status = f.cleaned_data['status']
                car.save()
            # to_update = car.update(carid=f.fields['carid'])
            #messages.success(request, "Cập nhật thành công!!!")
            # url = reverse('car_detail', args=(), kwargs={'url_id':car.id})
            return redirect('/admin/lich-trinh/chi-tiet/'+car_id)
        car = Schedule.objects.get(id = car_id)
        cF =  ScheduleForm() 
        # cF.fields['car'].initial = car.car
        # cF.fields['car'].label_from_instance = lambda obj: "%s (%s)" % (c.nameofcar, c.carid)
        # cF.fields['guess_name'].initial = car.guess_name
        # cF.fields['email'].initial = car.email
        # cF.fields['phone_number'].initial = car.phone_number
        cF.fields['departure_day'].initial = car.departure_day
        cF.fields['destination_day'].initial = car.destination_day
        cF.fields['departure'].initial = car.departure
        cF.fields['destination'].initial = car.destination

        cF.fields['departure_time'].initial = car.departure_time
        cF.fields['price'].initial = car.price
        cF.fields['deposit'].initial = car.deposit
        cF.fields['status'].initial = car.status
        return render(request, 'carservice/schedule/edit.html', {'form':cF})
    except Schedule.DoesNotExist:
        raise Http404("Khong tim thay xe")
    return render(request, 'carservice/schedule/edit.html', {'car':car})

def schedule_delete(request, car_id):
    try:
        c = Schedule.objects.get(id = car_id)
        c.delete()
        return redirect('../lich-trinh/')
    except Schedule.DoesNotExist:
        raise Http404("Khong tim thay xe")

# xong phan quan ly lich trinh
