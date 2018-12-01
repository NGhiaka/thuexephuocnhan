# from django.shortcuts import render, redirect

# # from .forms import RegisterForm
# from carservice.forms import *
# from carservice.models import *
# from django.contrib import messages
# from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import CustomerForm
from carservice.models import Customer
from django.contrib import messages

# from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect





class CustomerList(ListView):
    template_name = 'carservice/customer/index.html'
    model  = Customer
    ordering = ['id']
    paginate_by = 20

class CustomerDetail(DetailView):
    template_name = 'carservice/customer/show.html'
    model  = Customer

class CustomerCreate(CreateView):
    template_name = 'carservice/customer/form.html'
    # model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('carservice:customer')
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class CustomerUpdate(UpdateView):
    template_name = 'carservice/customer/form.html'
    form_class = CustomerForm
    model = Customer
    success_url = reverse_lazy('carservice:customer')
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'carservice/customer/delete.html'
    success_url = reverse_lazy('carservice:customer')
    # def post(self, request, *args, **kwargs):
    #     if "cancel" in request.POST:
    #         url = self.get_success_url()
    #         return HttpResponseRedirect(url)
    #     else:
    #         return super(CustomerDelete, self).post(request, *args, **kwargs)
    # 