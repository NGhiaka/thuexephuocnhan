from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import *
from carservice.models import *
from django.contrib import messages
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# lich trinh



class CarList(ListView):
    template_name = 'carservice/schedule/carlist.html'
    # model = Car
    form_class = CarForm
    paginate_by = 20
    ordering = ['id']
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        car = Car.objects.all()
        return render(request, self.template_name, {'form': form, 'cars': car})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('carservice:schedule_new', kwargs={'car_id': self.kwargs['car_id']}))
        return render(request, self.template_name, {'form': form})


class CustomerList(ListView):
    template_name = 'carservice/schedule/customerlist.html'
    # model  = Customer
    form_class = CustomerForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        customer = Customer.objects.all()
        return render(request, self.template_name, {'form': form, 'customers': customer})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('carservice:schedule_new', kwargs={
                'car_id': self.kwargs['car_id'],
                'customer_id': self.kwargs['customer_id']
                }))
        return render(request, self.template_name, {'form': form, 'customers': iter(self.model)})

class ScheduleList(ListView):
    template_name = 'carservice/schedule/index.html'
    model  = Schedule

def ScheduleCreate(request, car_id, customer_id):
    if not car_id or not customer_id:
        return HttpResponseRedirect(reverse_lazy('carservice:schedule_new'))
    if request.method == 'POST': 
        # car = Car.objects.get(id=car_id)
        f = ScheduleForm(request.POST)
        if f.is_valid(): 
            car = Car(id = car_id)
            customer = Customer(id=customer_id)
            sch = f.save(commit=False)
            sch.car = car
            sch.customer = customer
            sch.save()
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
            car = Schedule.objects.get(id=car_id)
            f = ScheduleForm(request.POST, instance=car)
            if f.is_valid(): 
                car.save()
            # to_update = car.update(carid=f.fields['carid'])
            messages.success(request, "Cập nhật thành công!!!")
            # url = reverse('car_detail', args=(), kwargs={'url_id':car.id})
            return redirect('/admin/lich-trinh/chi-tiet/'+car_id)
        car = Schedule.objects.get(id = car_id)
        cF =  ScheduleForm(instance=car) 
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
