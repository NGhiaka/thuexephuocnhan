# from django.shortcuts import render, redirect

# # from .forms import RegisterForm
# from carservice.forms import *
# from carservice.models import *
# from django.contrib import messages
from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import BlogFormset, CategoryForm, BlogForm
from carservice.models import Blog, Category
from django.contrib import messages

# from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages




class BlogIndex(ListView):
    template_name = 'carservice/blog/index.html'
    model  = Blog
    ordering = ['id']
    paginate_by = 1
    def get_context_data(self,**kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['Category_list'] = Category.objects.all()
        context['Blog_list'] = Blog.objects.all()
        return context
    
class BlogList(DetailView):
    template_name = 'carservice/blog/blog.html'
    model  = Category
    ordering = ['id']
    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        category = Category.objects.get(id = self.kwargs['pk'])
        context['blog_list'] = category.blog_set.all()  #laays tat ca blog trong cung 1 category
        context['category_id'] = self.kwargs['pk']
        return context

class BlogDetail(DetailView):
    template_name = 'carservice/blog/show.html'
    model  = Blog

# class BlogCreate(CreateView):
#     template_name = 'carservice/blog/form.html'
#     model = Blog
#     form_class = BlogFormset
#     success_url = '/admin/blog'

#     def get_context_data(self, **kwargs):
#         context = super(BlogCreate, self).get_context_data(**kwargs)
#         if self.kwargs['pk']:
#             category = Category.objects.filter(id = self.kwargs['pk'])
#             context['categories'] = category#category.blog_set.all()  #laays tat ca blog trong cung 1 category

#             context['category_id'] = self.kwargs['pk']
#         return context
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.typenews = self.request.typenews
#         return super(CreateArticle, self).form_valid(form)
def BlogCreate(request, pk = None):
    template_name = 'carservice/blog/form.html'
    if request.method == 'POST': 
        categoryID = request.POST.get('category', '') #lấy thông tin select value hoặc ''
        if categoryID != '': #nếu có id
            category = Category.objects.filter(id = categoryID)
            formset = BlogFormset(request.POST, request.FILES)

            if formset.is_valid():
                for form in formset:
                    blog = form.save(commit=False)
                    blog.category_id = categoryID
                    blog.author = request.user
                    blog.save()
                    messages.success(request, 'Thêm blog thành công!')
        else: # Thêm mới thể loại
            categoryform = CategoryForm(request.POST, request.FILES)
            formset = BlogFormset(request.POST, request.FILES)
            if categoryform.is_valid() and formset.is_valid():
                cate = categoryform.save()
                if formset:
                    for form in formset:
                        blog = form.save(commit=False)
                        blog.category = cate
                        blog.author = request.user
                        blog.save() 
                        messages.success(request, 'Thêm blog thành công!')
        # if formset.is_valid():
        #     if formset:
        #         for cate in formset:
        #             blog = formset.save(commit=False)
        #             blog.category = cate
        #             blog.save()
        return redirect('carservice:blog')
    categoryform = CategoryForm()
    formset = BlogFormset(queryset=Blog.objects.none())
    if pk:
        category = Category.objects.get(id = pk)
        return render(request, template_name, {
            'category': category,
            'categoryform': categoryform,
            'formset': formset,
        })
    categories = Category.objects.all()
    return render(request, template_name, {
            'categories': categories,
            'categoryform': categoryform,
            'formset': formset,
        })

def BlogUpdate(request, pk):
    template_name = 'carservice/blog/form.html'
    blog = Blog.objects.get(id = pk)
    if request.method == 'POST': 
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, 'Cập nhật thành công!')
        return redirect('carservice:blog')

    
    formset = BlogForm(instance=blog)
    return render(request, template_name, {
        'category': blog.category,
        'formset': formset
    })
    #  
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class BlogDelete(DeleteView):
    model = Blog
    template_name = 'carservice/blog/delete.html'
    success_url = reverse_lazy('carservice:blog')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/admin/login')
        return HttpResponse('Hello, World!')
    # def post(self, request, *args, **kwargs):
    #     if "cancel" in request.POST:
    #         url = self.get_success_url()
    #         return HttpResponseRedirect(url)
    #     else:
    #         return super(AuthorDelete, self).post(request, *args, **kwargs)

    
        
