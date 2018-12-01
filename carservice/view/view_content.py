# from .forms import RegisterForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from carservice.forms import ContentForm
from carservice.models import Content
from django.urls import reverse_lazy



# from django.core.urlresolvers import reverse_lazy


# def content(request):
#     content_list = Content.objects.all().order_by('id')
#     context = {
#         'content_list': content_list,
#     }
#     return render(request, 'carservice/content/index.html', context)
        
# def content_new(request):
#     if request.method == 'POST': 
#         f = ContentForm(request.POST)
#         od = f.save()
#         messages.success(request, "Thêm thành công!!!")
#         return redirect('/admin/noidung')
#     cF =  ContentForm() 
#     return render(request, 'carservice/content/new.html', {'form':cF})

# def content_edit(request, content_id):
#     try:
        
#         if request.method == 'POST': 
#             f = ContentForm(request.POST)
#             if f.is_valid(): 
#                 content = Content.objects.get(id=content_id)
#                 content.avatar = f.cleaned_data['avatar']
#                 content.title = f.cleaned_data['total_revenue']
#                 content.phone = f.cleaned_data['phone']
#                 content.email = f.cleaned_data['email']
#                 content.link = f.cleaned_data['link']
#                 content.summary = f.cleaned_data['summary']
#                 content.save()
#             # to_update = content.update(contentid=f.fields['contentid'])
#             #messages.success(request, "Cập nhật thành công!!!")
#             # url = reverse('content_detail', args=(), kwargs={'url_id':content.id})
#             return redirect('/admin/noidung/')
#         content = Content.objects.get(id = content_id)
#         cF =  ContentForm() 
#         cF.fields['avatar'].initial = content.avatar
#         cF.fields['title'].initial = content.title
#         cF.fields['phone'].initial = content.phone
#         cF.fields['email'].initial = content.email
#         cF.fields['link'].initial = content.link
#         cF.fields['summary'].initial = content.summary
        
#         return render(request, 'carservice/content/edit.html', {'form':cF})
#     except content.DoesNotExist:
#         raise Http404("Khong tim thay xe")
#     return render(request, 'carservice/content/edit.html', {'content':content})

#####UNG DUNG CLASS BASE

class ContentList(ListView):
    template_name = 'carservice/content/index.html'
    model  = Content
    ordering = ['id']
    paginate_by = 20

class ContentCreate(CreateView):
    template_name = 'carservice/content/form.html'
    model = Content
    form_class = ContentForm
    success_url = '/admin/noidung'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class ContentUpdate(UpdateView):
    template_name = 'carservice/content/form.html'
    form_class = ContentForm
    model = Content
    success_url = reverse_lazy('carservice:content')
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

class ContentDelete(DeleteView):
    model = Content
    template_name = 'carservice/content/delete.html'
    success_url = reverse_lazy('carservice:content')
    # def post(self, request, *args, **kwargs):
    #     if "cancel" in request.POST:
    #         url = self.get_success_url()
    #         return HttpResponseRedirect(url)
    #     else:
    #         return super(AuthorDelete, self).post(request, *args, **kwargs)
    
    #     