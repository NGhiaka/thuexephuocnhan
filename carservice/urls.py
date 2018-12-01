from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .view import *
# from .view import view_car, view_cost, view_driver, view_photo, view_schedule, view_content, view_blog, view_customer, view_type_news
app_name = "carservice"
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^quan-ly-xe/$', view_car.CarList.as_view(), name='car'),
	url(r'^quan-ly-xe/them-xe$', view_car.CarCreate.as_view(), name='car_new'),
	# url(r'^quan-ly-xe/them-xe$', view_car.car_new, name='car_new'),
	url(r'^quan-ly-xe/chi-tiet/(?P<pk>\d+)$', view_car.CarDetail.as_view(), name='car_detail'),
	url(r'^quan-ly-xe/cap-nhat/(?P<pk>\d+)$', view_car.CarUpdate.as_view(), name='car_edit'),
	url(r'^quan-ly-xe/xoa/(?P<pk>\d+)$', view_car.CarDelete.as_view(), name='car_delete'),


	url(r'^tai-xe/$', view_driver.DriverList.as_view(), name='driver'),
	url(r'^tai-xe/them-tai-xe$', view_driver.DriverCreate.as_view(), name='driver_new'),
	url(r'^tai-xe/chi-tiet/(?P<pk>[0-9]+)/$', view_driver.DriverDetail.as_view(), name='driver_detail'),
	url(r'^tai-xe/cap-nhat/(?P<pk>[0-9]+)/$', view_driver.DriverUpdate.as_view(), name='driver_edit'),
	url(r'^tai-xe/xoa/(?P<pk>[0-9]+)/$', view_driver.DriverDelete.as_view(), name='driver_delete'),


	url(r'^album/$', view_photo.AlbumList.as_view(), name='album'),
	url(r'^album/them$', view_photo.album_new, name='album_new'),
	url(r'^album/chi-tiet/(?P<pk>[0-9]+)/$', view_photo.album_detail, name='album_detail'),
	url(r'^album/cap-nhat/(?P<pk>[0-9]+)/$', view_photo.album_edit, name='album_edit'),
	url(r'^album/xoa/(?P<pk>[0-9]+)/$', view_photo.album_delete, name='album_delete'),

	url(r'^anh/$', view_photo.PhotoList.as_view(), name='photo'),
	url(r'^anh/them/(?P<pk>[0-9]+)/$', view_photo.photo_new, name='album_photo_new'),
	url(r'^anh/chi-tiet/(?P<pk>[0-9]+)/$', view_photo.photo_detail, name='album_photo_detail'),
	url(r'^anh/cap-nhat/(?P<pk>[0-9]+)/$', view_photo.photo_edit, name='album_photo_edit'),
	url(r'^anh/xoa/(?P<pk>[0-9]+)/$', view_photo.photo_delete, name='album_photo_delete'),

	url(r'^lich-trinh/$', view_schedule.ScheduleList.as_view(), name='schedule'),
	url(r'^lich-trinh/them/chon-xe/$', view_schedule.CarList.as_view(), name='schedule_choose'),
	url(r'^lich-trinh/them/chon-khach-hang/(?P<car_id>[0-9]+)$', view_schedule.CustomerList.as_view(), name='schedule_choose'),
	url(r'^lich-trinh/them/(?P<car_id>[0-9]+)/(?P<customer_id>[0-9]+)$', view_schedule.schedule_new, name='schedule_new'),
	url(r'^lich-trinh/chi-tiet/(?P<car_id>[0-9]+)/$', view_schedule.schedule_detail, name='schedule_detail'),
	url(r'^lich-trinh/cap-nhat/(?P<car_id>[0-9]+)/$', view_schedule.schedule_edit, name='schedule_edit'),
	url(r'^lich-trinh/xoa/(?P<car_id>[0-9]+)/$', view_schedule.schedule_delete, name='schedule_delete'),


	url(r'^chi-phi/$', view_cost.CostList.as_view(), name='cost'),
	url(r'^chi-phi/them$', view_cost.CostCreate.as_view(), name='cost_new'),
	url(r'^chi-phi/chi-tiet/(?P<cost_id>[0-9]+)$', view_cost.CostDetail.as_view(), name='cost_detail'),
	url(r'^chi-phi/cap-nhat/(?P<cost_id>[0-9]+)$', view_cost.CostUpdate.as_view(), name='cost_edit'),
	url(r'^chi-phi/xoa/(?P<cost_id>[0-9]+)$', view_cost.CostDelete.as_view(), name='cost_delete'),


	# url(r'^chi-phi/them/$', view_cost.cost_new, name='cost_new'),
	# url(r'^chi-phi/chi-tiet/(?P<cost_id>[0-9]+)$', view_cost.cost_detail, name='cost_detail'),
	# url(r'^chi-phi/cap-nhat/(?P<cost_id>[0-9]+)$', view_cost.cost_edit, name='cost_edit'),
	# url(r'^chi-phi/xoa/(?P<cost_id>[0-9]+)/$', view_cost.cost_delete, name='cost_delete'),

	# url(r'^chiphi/json$', views.schedule_json, name='schedule_json'),
	url(r'^khach-hang/$', view_customer.CustomerList.as_view(), name='customer'),
	url(r'^khach-hang/them/$', view_customer.CustomerCreate.as_view(), name='customer_new'),
	url(r'^khach-hang/chi-tiet/(?P<pk>\d+)$', view_customer.CustomerDetail.as_view(), name='customer_detail'),
	url(r'^khach-hang/cap-nhat/(?P<pk>\d+)$', view_customer.CustomerUpdate.as_view(), name='customer_edit'),
	url(r'^khach-hang/xoa/(?P<pk>\d+)$', view_customer.CustomerDelete.as_view(), name='customer_delete'),



	url(r'^dich-vu/$', views.service, name='service'),
	url(r'^chi-phi/$', views.statistical_income, name='statistical_income'),

	# url(r'^noidung/$', view_content.content, name='content'),
	# url(r'^noidung/them$', view_content.content_new, name='content_new'),
	# url(r'^noidung/capnhat$', view_content.content_edit, name='content_edit'),

	url(r'^noi-dung/$', view_content.ContentList.as_view(), name='content'),
	url(r'^noi-dung/them/$', view_content.ContentCreate.as_view(), name='content_new'),
	url(r'^noi-dung/cap-nhat/(?P<pk>\d+)$', view_content.ContentUpdate.as_view(), name='content_edit'),


	url(r'', include('django.contrib.auth.urls'), name='login'),
	#url(r'^dangnhap/$', views.login, name='login'),
    url(r'^dang-ky/$', views.signup, name='signup'),
    # url(r'^dangnhap/$', views.login, name='login'),

    url(r'^tin-tuc/$', view_blog.BlogIndex.as_view(), name='blog'),
    url(r'^tin-tuc/the-loai/(?P<pk>\d+)$', view_blog.BlogList.as_view(), name='blog_list'),
	url(r'^tin-tuc/them/$', view_blog.BlogCreate, name='blog_new'),
	url(r'^tin-tuc/them/(?P<pk>\d*)$', view_blog.BlogCreate, name='blog_new'),

	url(r'^tin-tuc/chi-tiet/(?P<pk>\d+)$', view_blog.BlogDetail.as_view(), name='blog_detail'),
	url(r'^tin-tuc/cap-nhat/(?P<pk>\d+)$', view_blog.BlogUpdate.as_view(), name='blog_edit'),
	url(r'^tin-tuc/xoa/(?P<pk>\d+)$', view_blog.BlogDelete.as_view(), name='blog_delete'),

	url(r'^the-loai-tin-tuc/$', view_type_news.CategoryList.as_view(), name='category'),
	url(r'^the-loai-tin-tuc/them$', view_type_news.CategoryCreate.as_view(), name='category_new'),
	url(r'^the-loai-tin-tuc/chi-tiet/(?P<pk>\d+)$', view_type_news.CategoryDetail.as_view(), name='category_detail'),
	url(r'^the-loai-tin-tuc/cap-nhat/(?P<pk>\d+)$', view_type_news.CategoryUpdate.as_view(), name='category_edit'),
	url(r'^the-loai-tin-tuc/xoa/(?P<pk>\d+)$', view_type_news.CategoryDelete.as_view(), name='category_delete'),
]
