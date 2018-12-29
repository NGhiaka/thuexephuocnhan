from django.conf.urls import url
 
from . import views
app_name = "frontend"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^trang-chu/$', views.home, name='home'),
    url(r'^gioi-thieu/$', views.AboutList.as_view(), name='about'),
    url(r'^dat-lich/$', views.BookingShow.as_view(), name='booking'),
    url(r'^dat-lich/tim$', views.BookingCreate.as_view(), name='create_booking'),

    url(r'^thong-tin-xe/$', views.CarList.as_view(), name='car'),
    url(r'^thong-tin-xe/(?P<pk>\d+)$', views.CarDetail.as_view(), name='detail_car'),

    url(r'^tin-tuc/$', views.BlogList.as_view(), name='news'),
    url(r'^tin-tuc/(?P<pk>\d+)$', views.BlogDetail.as_view(), name='detail_news'),
    
    url(r'^lien-he/$', views.ContactList.as_view(), name='contact'),
]