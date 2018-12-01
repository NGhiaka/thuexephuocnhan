from django.shortcuts import render, redirect

# from .forms import RegisterForm
from carservice.forms import *
from carservice.models import *
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy



# def handle_uploaded_file(file, filename):
#     # if not os.path.exists('upload/'):
#     #     os.mkdir('upload/')
#     with open(filename, 'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)


# quan ly anh
class AlbumList(ListView):
    template_name = 'carservice/album/index.html' 
    model = Album
    ordering = ['id']
    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        context['album_list'] = Album.objects.all()
        context['photo_list'] = Photo.objects.all()
        return context
# class AlbumDetail(DetailView):
#     template_name = 'carservice/album/show.html'
#     model  = Driver

# class AlbumCreate(CreateView):
#     template_name = 'carservice/album/form.html'
#     model = Driver
#     form_class = DriverForm
#     success_url = '/admin/album'
    # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

# class AlbumUpdate(UpdateView):
#     template_name = 'carservice/album/form.html'
#     model = Driver
#     form_class = DriverForm
#     success_url = '/admin/taixe'
#     # fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']

# class AlbumDelete(DeleteView):
#     model = Driver
#     template_name = 'carservice/album/delete.html'
#     success_url = reverse_lazy('carservice:album')


# def album(request):
#     album_list = Album.objects.all().order_by('id')
#     context = {
#         'album_list': album_list,
#     }
#     return render(request, 'carservice/album/index.html', context)
        
def album_new(request):
    template_name = 'carservice/album/form.html'
    if request.method == 'GET':
        albumform = AlbumForm(request.GET or None)
        formset = PhotoFormset(queryset=Photo.objects.none())
    elif request.method == 'POST': 
        albumform = AlbumForm(request.POST, request.FILES)
        formset = PhotoFormset(request.POST, request.FILES)
        if albumform.is_valid() and formset.is_valid():
            album = albumform.save()
            if formset:
                for photoform in formset:
                    photo = photoform.save(commit=False)
                    photo.album = album
                    photo.save()
            return redirect('carservice:album')
    return render(request, template_name, {
        'albumform': albumform,
        'formset': formset,
    })

def album_detail(request, pk):
    try:
        photo_list = Photo.objects.filter(album = pk)
        album = Album.objects.get(id = pk)
        context = {
            'photo_list': photo_list,
            'album_name' : album,
        }
        return render(request, 'carservice/album/show.html', context)
    except Album.DoesNotExist:
        raise Http404("Question does not exist")
def album_edit(request, pk):
    try:    
        if request.method == 'POST': 
            f = AlbumForm(request.POST, request.FILES)
            if f.is_valid(): 
                f.save()
          
            return redirect('/admin/album/chi-tiet/'+pk)
        album = Album.objects.get(id = pk)
        albumForm =  AlbumForm(instance=album)
        
        return render(request, 'carservice/album/edit.html', {'form':albumForm})
    except Album.DoesNotExist:
        raise Http404("Khong tim thay xe")
def album_delete(request, pk):
    try:
        d = Album.objects.get(id = pk)
        p = Photo.objects.filter(album = d)
        d.delete()
        p.delete()
        return redirect('/admin/album/')
    except Album.DoesNotExist:
        raise Http404("Khong tim thay album")

class PhotoList(ListView):
    template_name = 'carservice/photo/index.html'
    model  = Photo
    ordering = ['id']
    paginate_by = 20
        
def photo_new(request, pk):
    template_name = 'carservice/album/form.html'
    if request.method == 'POST': 
        album = Album.objects.get(id = pk)
        formset = PhotoFormset(request.POST, request.FILES)
        if formset.is_valid():
            for photoform in formset:
                photo = photoform.save(commit=False)
                photo.album = album
                photo.save()
    #         handle_uploaded_file(path_img, str(path_img))
            return redirect('carservice:album')
    album = Album.objects.get(id=pk)
    albumform = AlbumForm(instance=album)
    formset = PhotoFormset(queryset=Photo.objects.none())
    return render(request, template_name, {
        'albumform': albumform,
        'formset': formset,
    })
def photo_detail(request, pk):
    try:
        al = Photo.objects.get(id = pk)
        return render(request, 'carservice/photo/show.html', {'al':al})
    except Photo.DoesNotExist:
        raise Http404("Question does not exist")
def photo_edit(request, pk):
    try:    
        if request.method == 'POST': 
            f = PhotoForm(request.POST, request.FILES)
            if f.is_valid(): 
                al = Photo.objects.get(id=pk)
                al.album = f.cleaned_data['album']
                al.path_img = f.cleaned_data['path_img']
                al.comment_img = f.cleaned_data['comment_img']
                al.save()
          
            return redirect('/admin/anh/chitiet/'+pk)
        al = Photo.objects.get(id = pk)
        dF =  PhotoForm() 
        dF.fields['album'].initial = al.album
        dF.fields['path_img'].initial = al.path_img
        dF.fields['comment_img'].initial = al.comment_img
        
        return render(request, 'carservice/photo/edit.html', {'form':dF})
    except Photo.DoesNotExist:
        raise Http404("Khong tim thay anh")
    return render(request, 'carservice/photo/edit.html', {'driv':driv})

def photo_delete(request, pk):
    try:
        d = Photo.objects.get(id=pk)
        album_id =  d.album.id
        d.delete()
        return redirect('/admin/album/chi-tiet/' + str(album_id).strip())
    except Photo.DoesNotExist:
        raise Http404("Khong tim thay photo")