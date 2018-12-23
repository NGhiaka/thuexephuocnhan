# from django.shortcuts import render, redirect

# # from .forms import RegisterForm
# from carservice.forms import *
# from carservice.models import *
# from django.contrib import messages
# from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import CarForm, PhotoCarForm
from carservice.models import Car, PhotoCar
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse
# from django.urls import reverse


from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import JsonResponse
from django.views import View


# from django.core.files.storage import default_storage

class CarList(ListView):
    template_name = 'carservice/car/index.html'
    model  = Car
    paginate_by = 20
    ordering = ['id']

class CarDetail(DetailView):
    template_name = 'carservice/car/show.html'
    model = Car

class CarCreate(CreateView):
    template_name = 'carservice/car/form.html'
    form_class = CarForm
    # success_url = reverse_lazy('carservice:car')
    def get_success_url(self):
        return reverse('carservice:car')
    # def get_redirect_url(self, **kwargs):
    #     params = self.kwargs
    #     name = self.kwargs.get('carservice:car_detail')
    #     if name:
    #       del params['carservice:car_detail']
    #       return reverse_lazy(name, kwargs=params)
    #     else:
    #       raise (ValueError, "redirectname not set in RedirectViewCustom call.")
        # def get_success_url(self):
        #     return reverse_lazy('carservice:car_detail', kwargs={'pk': self._id})
    
class CarUpdate(UpdateView):
    template_name = 'carservice/car/form.html'
    form_class = CarForm
    model = Car
    success_url = reverse_lazy('carservice:car')

class CarDelete(DeleteView):
    model = Car
    template_name = 'carservice/car/delete.html'
    success_url = reverse_lazy('carservice:car')
    # def post(self, request, *args, **kwargs):
    #     if "cancel" in request.POST:
    #         url = self.get_success_url()
    #         return HttpResponseRedirect(url)
    #     else:
    #         return super(AuthorDelete, self).post(request, *args, **kwargs)
    
# def car_new(request):
#     if request.method == 'POST': 
#         f = CarForm(request.POST, request.FILES)
#         if f.is_valid():
#             f.save()
#         messages.success(request, "Thêm thành công!!!")
#         return redirect('/admin/quan-ly-xe')
#     cF =  CarForm() 
#     return render(request, 'carservice/car/car_form.html', {'form':cF})

# def car_detail(request, car_id):
#     try:
#         car = Car.objects.get(id = car_id)
#     except Car.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'carservice/car/show.html', {'car':car})
# def car_edit(request, car_id):
#     try:
        
#         if request.method == 'POST': 
#             f = CarForm(request.POST, request.FILES)
#             if f.is_valid(): 
#                 car = Car.objects.get(id=car_id)
#                 car.carid = f.cleaned_data['carid']
#                 car.nameofcar = f.cleaned_data['nameofcar']
#                 car.manufacturer = f.cleaned_data['manufacturer']
#                 car.owner = f.cleaned_data['owner']
#                 car.typecar = f.cleaned_data['typecar']
#                 car.yearofmanu = f.cleaned_data['yearofmanu']
#                 car.avatar = f.cleaned_data['avatar']
#                 car.save()
#             # to_update = car.update(carid=f.fields['carid'])
#             #messages.success(request, "Cập nhật thành công!!!")
#             # url = reverse('car_detail', args=(), kwargs={'url_id':car.id})
#             return redirect('/admin/quanlyxe/chitiet/'+car_id)
#         car = Car.objects.get(id = car_id)
#         cF =  CarForm() 
#         cF.fields['carid'].initial = car.carid
#         cF.fields['nameofcar'].initial = car.nameofcar
#         cF.fields['manufacturer'].initial = car.manufacturer
#         cF.fields['owner'].initial = car.owner
#         cF.fields['typecar'].initial = car.typecar
#         cF.fields['yearofmanu'].initial = car.yearofmanu
#         cF.fields['avatar'].initial = car.avatar
#         return render(request, 'carservice/car/edit.html', {'form':cF})
#     except Car.DoesNotExist:
#         raise Http404("Khong tim thay xe")
#     return render(request, 'carservice/car/edit.html', {'car':car})

# def car_delete(request, car_id):
#     try:
#         c = Car.objects.get(id = car_id)
#         c.delete()
#         return redirect('../quanlyxe/')
#     except Car.DoesNotExist:
#         raise Http404("Khong tim thay xe")

# # xong phan quan ly xe

# class PhotoCreate(ListView):
#     """docstring for Phôt"""
#     template_name = 'carservice/car/photoform.html'
#     form_class = PhotoCarForm
#     def post(self, request, *args, **kwargs):
#         car = Car(id= self.kwargs["pk"])
#         forms = PhotoCarForm(self.request.FILES)
#         if forms.is_valid():
#             for f in forms:
#                 photo = f.save()
#                 photo.car = car
#                 photo.save()
#                 data = {'is_valid': True, 'name': photo.path_img.name, 'url': photo.path_img.url}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)
        

class PhotoCreate(ListView):
    template_name = 'carservice/car/photoform.html'
    form_class = PhotoCarForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        # photos_list = PhotoCar.objects.filter(car_id= self.kwargs["pk"])
        return render(request, self.template_name, {'form': form, 'carid': self.kwargs["pk"]})
    def post(self, request, *args, **kwargs):
        car = Car.objects.get(pk = self.kwargs["pk"])
        for img in request.FILES.getlist('path_img'):
            ph = PhotoCar()
            ph.car= car 
            ph.path_img = img
            ph.save()
        messages.success(request,
                             "Yeeew, check it out on the home page!")
        return HttpResponseRedirect(reverse_lazy('carservice:car'))

        # forms = PhotoCarForm(self.request.FILES)
        # if forms.is_valid():
        #     for form in forms.cleaned_data:
        #         photo = form['path_img']
        #         photocar = PhotoCar(car=car, path_img=photo)
        #         photocar.save()
        #         # data = {'is_valid': True, 'name': photocar.path_img.name, 'url': photocar.path_img.url}
        #     messages.success(request,
        #                      "Yeeew, check it out on the home page!")
        #     return reverse_lazy('carservice:car')
        # else:
        #     data = {'is_valid': False}
        # return JsonResponse(data)