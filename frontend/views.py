from django.shortcuts import render
from carservice.forms import *
from carservice.models import *
# from carservice.models import *
import datetime
# from django.utils.timezone import datetime
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.db.models import F, Q, Count



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
	cars = Car.objects.order_by('-yearofmanu').all()[:8]
	blogs = Blog.objects.order_by('-dateSubmit').all()[:5]
	context = {
		'cars': cars,
		'blogs': blogs,
	}
	return render(request, 'frontend/home.html', context)
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
	ordering = ['id']
	paginate_by = 15
	def get(self, request, *args, **kwargs):
		typeCar = request.GET.get('typecar', None)
		start_date = request.GET.get('startDate', None)
		end_date = request.GET.get('endDate', None)
		if start_date != '' and start_date is not None:
			start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
		if end_date != '' and end_date is not None:
			end_date = datetime.datetime.strptime(end_date, '%d/%m/%Y').strftime('%Y-%m-%d') 
		car = Car.objects.all()
		if typeCar is not None and typeCar != '':
			car = car.filter(Q(typecar = typeCar))
		if (start_date is not None and end_date is not None) and (end_date != '' and start_date != ''):
			car = car.filter(
					~Q(schedule__departure_day__range=(start_date, end_date)),
					~Q(schedule__destination_day__range=(start_date, end_date)),
					~Q(schedule__departure_day__lte=start_date, schedule__destination_day__gte=start_date),
					~Q(schedule__departure__lte=end_date, schedule__destination__gte=end_date)
				)
			# car = Car.objects.filter(Q(schedule__id__isnull=True),Q(typecar = typeCar), 
			# 	Q(schedule__departure_day__range=(start_date, end_date))
			# 	| Q(schedule__destination_day__range=(start_date, end_date))
			# 	| Q(schedule__departure_day__lte=start_date, schedule__destination_day__gte=start_date)
			# 	| Q(schedule__departure__lte=end_date, schedule__destination__gte=end_date)
			# )

		return render(request, self.template_name, {'object_list':car})
		


class CarDetail(DetailView):
	template_name = 'frontend/car_detail.html'
	model  = Car
	def get_context_data(self, **kwargs):
		context = super(CarDetail, self).get_context_data(**kwargs)		
		car = self.object
		context['car'] = car
		context['photos'] = PhotoCar.objects.filter(car=car)
		context['other_cars'] = Car.objects.filter(~Q(id=car.id))[:5]
		return context

class BlogList(ListView):
	template_name = 'frontend/news.html'
	model  = Blog #News
	ordering = ['id']
	paginate_by = 15
	context_object_name = "blog_list"
	def get_context_data(self, **kwargs):
		context = super(BlogList, self).get_context_data(**kwargs)
		categories = Category.objects.all()
		context['categories'] = categories
		return context

class BlogDetail(DetailView):
	template_name = 'frontend/news_detail.html'
	model  = Blog #News		
	def get_context_data(self, **kwargs):
		context = super(BlogDetail, self).get_context_data(**kwargs)
		Blog.objects.filter(id = self.kwargs['pk']).update(view=F('view')+1)
		blog = Blog.objects.get(id = self.kwargs['pk'])
		context['blog'] = blog  #laays tat ca blog trong cung 1 category
		context['blog_category'] = Blog.objects.order_by('-id').filter(category=blog.category).filter(~Q(id=blog.id))[:3]
		context['blog_most'] = Blog.objects.order_by('-view').filter(~Q(id=blog.id))[:5]
		context['categories'] = Category.objects.all().annotate(blogs_count=Count('blog'))
		return context
	


class ContactList(ListView):
	template_name = 'frontend/contact.html'
	model  = Content #Booking




def handler404(request):
    return render(request, 'frontend/page/404.html', status=404)

def handler500(request):
    return render(request, 'frontend/page/500.html', status=500)