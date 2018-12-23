from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


# from .forms import RegisterForm
from carservice.forms import *
from carservice.models import *
from django.contrib import messages

from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView
from django.urls import reverse_lazy

 
class ExpenseList(ListView):
    template_name = 'carservice/expense/index.html'
    model  = Expense
    ordering = ['id']
    paginate_by = 20

def ExpenseCreate(request):
    template_name = 'carservice/expense/form.html'
    form = ExpenseForm(request.POST or None)
    if request.method == 'POST': 
        form = ExpenseForm(request.POST)
        if form.is_valid(): 
            exp = form.save(commit=False)
            exp.author = request.user
            exp.save()
            messages.success(request, "Thêm thành công!!!")
            return HttpResponseRedirect(reverse_lazy('carservice:expense'))
        messages.error(request, "Tạo  công!!!")
    return render(request, template_name, {'form':form})

# class ExpenseCreate(CreateView):
#     template_name = 'carservice/expense/form.html'
#     form_class = ExpenseForm
#     # initial = {'key': 'value'}
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             exp = form.save(commit=False)
#             exp.author = request.user
#             exp.save()
#             # return super(ExpenseCreate, self).post(form)

#         return reverse_lazy('carservice:expense')

        # return render(request, self.template_name, {'form': form})

class ExpenseDetail(DetailView):
    template_name = 'carservice/expense/show.html'
    model  = Expense

def ExpenseUpdate(request, pk):
    template_name = 'carservice/expense/form.html'
    instance = Expense.objects.get(id = pk)
    if request.method == 'POST': 
        form = ExpenseForm(request.POST, instance=instance)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.author = request.user
            exp.save()
            messages.success(request, "Thêm thành công!!!")    
            return HttpResponseRedirect(reverse('carservice:expense'))
        return render(request, template_name, {'form': form})
    form = ExpenseForm(instance=instance)
    return render(request, template_name, {'form': form})

# class ExpenseDelete(DeleteView):
#     template_name = 'carservice/expense/delete.html'
#     model = Expense
#     success_url = reverse_lazy('carservice:expense')
def ExpenseDelete(request, pk):
    try:
        d = Expense.objects.get(id=pk)
        d.delete()
        messages.success(request, "Thêm thành công!!!")
        return HttpResponseRedirect(reverse("carservice:expense"))
    except Photo.DoesNotExist:
        raise Http404("Khong tim thay photo")