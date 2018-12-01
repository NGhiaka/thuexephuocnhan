from django.shortcuts import render
from carservice.forms import *
from carservice.models import *
# from carservice.models import *
from django.utils.timezone import datetime
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


# from django.http import JsonResponse
# from django.views.generic.edit import CreateView
# Create your views here.

# def index(request):
# 	content = Content.objects.all()
#     context = { 'content': content, }
#     return render(request, 'frontend/index.htm', context)\


# def index(request):
# 	# today = datetime.today()
# 	# ct = Content.objects.all().order_by('id')
# 	# imgs = Photo.objects.all().order_by('id')
# 	# cars = Car.objects.all()
# 	# schs = Schedule.objects.filter(destination_day__gte = today)
# 	# context = {
# 	# 	'contents': ct,
# 	# 	'images' : imgs,
# 	# 	'cars' : cars,
# 	# 	'schedules' : schs,

# 	# }
# 	return render(request, 'frontend/index.html')
def index(request):
	return render(request, 'frontend/index.html')
# class index(ListView):
# 	template_name = 'frontend/index.html'
	# model  = Content

def home(request):
	return render(request, 'frontend/home.html')
#Hien thi thong tin trang web
class AboutList(ListView):
	template_name = 'frontend/about.html'
	model  = Content

#Khi search thong tin tra ve nhung chiec xe co lich trong 


class BookingShow(ListView):
	template_name = 'frontend/booking.html'
	model  = Schedule
	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['latest_articles'] = Article.objects.all()[:5]
	# 	return context

class BookingCreate(CreateView):
	template_name = 'frontend/create_booking.html'
	model  = Schedule #Booking	


#Hien thi thong tin cua tung chiec xe
class CarList(ListView):
	template_name = 'frontend/car.html'
	model  = Car

class CarDetail(DetailView):
	template_name = 'frontend/car_detail.html'
	model  = Car

class BlogList(ListView):
	template_name = 'frontend/news.html'
	model  = Blog #News
	ordering = ['id']
	def get_context_data(self, **kwargs):
		context = super(BlogList, self).get_context_data(**kwargs)
		categories = Category.objects.all()
		context['blog_list'] = Blog.objects.all()  #laays tat ca blog trong cung 1 category
		context['categories'] = categories
		return context

class BlogDetail(DetailView):
	template_name = 'frontend/news_detail.html'
	model  = Blog #News		


class ContactList(ListView):
	template_name = 'frontend/contact.html'
	model  = Content #Booking