# from django.shortcuts import render, redirect

# # from .forms import RegisterForm
# from carservice.forms import *
# from carservice.models import *
from django.contrib import messages
# from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import CategoryForm
from carservice.models import Category
from django.contrib import messages

# from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView
from django.urls import reverse_lazy





class CategoryList(ListView):
    template_name = 'carservice/typenews/index.html'
    model  = Category
    ordering = ['id']
    paginate_by = 20

class CategoryDetail(DetailView):
    template_name = 'carservice/typenews/show.html'
    model  = Category

class CategoryCreate(CreateView):
    template_name = 'carservice/typenews/form.html'
    model = Category
    form_class = CategoryForm
    success_url = '/admin/tin-tuc/them'
    def __init__(self):
        self.success_url = '/admin/tin-tuc/them'

    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class CategoryUpdate(UpdateView):
    template_name = 'carservice/typenews/form.html'
    form_class = CategoryForm
    model = Category
    success_url = '/admin/tin-tuc/them'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('carservice:blog')
    template_name = 'carservice/blog/delete.html'
    
        
