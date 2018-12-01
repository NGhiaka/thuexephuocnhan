from django import forms
from django.forms import ModelForm
from carservice.models import *
from django.utils.translation import ugettext_lazy as _
# from phonenumber_field import widgets
# from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory, inlineformset_factory, modelformset_factory


MANU_CHOOSE = (('AUDI','AUDI'), ('BMW','BMW'), ('CHEVROLET','CHEVROLET'),('FORD','FORD'),('TOYOTA','TOYOTA'),( 'HONDA', 'HONDA'),('HYUNDAI','HYUNDAI') , ('ISUZU','ISUZU'),('KIA','KIA') , ('LAND ROVER','LAND ROVER'),('LEXUS','LEXUS') ,('MAZDA','MAZDA') , ('MERCEDES-BENZ','MERCEDES-BENZ'),('MITSUBISHI','MITSUBISHI') ,('NISSAN','NISSAN') , ('PEUGEOT','PEUGEOT'),('PORSCHE','PORSCHE') ,('RENAULT','RENAULT') , ('SUZUKI','SUZUKI'), ('VOLKSWAGEN','VOLKSWAGEN'), ('FUSO','FUSO'), ('HINO','HINO'), ('INFINITI','INFINITI'), ('JAGUAR','JAGUAR'), ('LAMBORGINI','LAMBORGINI'), ('LUXGEN','LUXGEN'), ('MASERATI','MASERATI'), ('MINI','MINI'), ('ROLLS ROYCE','ROLLS ROYCE'), ('SAMSUNG','SAMSUNG'), ('SUBARU','SUBARU'), ('SYM','SYM'), ('THACO','THACO'), ('VINAXUKI','VINAXUKI'), ('VOLVO','VOLVO'))
permision_choose = ((1, 'Chỉ được thêm mới dữ liệu'), (2, 'Được thêm, xóa, sửa dữ liệu'))
TYPE_CAR = (("4 Chỗ", "4 Chỗ"), ("7 Chỗ", "7 Chỗ"), ("9 Chỗ", "9 Chỗ"), ("16 Chỗ", "16 Chỗ"),("29 Chỗ", "29 Chỗ"), ("45 Chỗ", "45 Chỗ"),  ("Xe giường nằm", "Xe giường nằm"))
class CarForm(ModelForm):
	"""docstring for Contacts"""
	class Meta:
		model = Car
		fields = ['carid', 'nameofcar', 'locate_code', 'manufacturer','owner', 'typecar', 'yearofmanu', 'avatar', 'about_car', ]
		labels = {
			'carid' : _('Biển số xe'),
			'nameofcar' : _("Tên xe"),
			'manufacturer' : _("Hãng xe"),
			'owner' : _("Chủ sở hữu"),
			'typecar' : _("Loại xe"),
			'yearofmanu' : _("Đời xe"),
			'avatar' : _("Ảnh đại diện"),
			'locate_code' : _("Mã định vị"),
			'about_car' : _("Giới thiệu"),
		}
		widgets = {
			'carid': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nhập biển số xe', 'name': 'carid'}),
			'nameofcar': forms.TextInput(attrs={'class': 'form-control','placeholder': 'ví dụ: Fortuner', 'name': 'nameofcar'}),
			'manufacturer' : forms.Select(choices = MANU_CHOOSE, attrs={'class': 'form-control select2', 'name': 'manufacturer'}), #forms.Select(attrs={'class': 'form-control', 'name': 'manufacturer'Ư)
			'owner': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nguyễn Văn Tèo', 'name': 'owner'}),
			'typecar': forms.Select(choices = TYPE_CAR, attrs={'class': 'form-control', 'name': 'typecar'}),
			# 'typecar': forms.TextInput(attrs={'class': 'form-control','placeholder': '16 chỗ', 'name': 'typecar'}),
            'yearofmanu': forms.TextInput(attrs={'class': 'form-control', 'name': 'yearofmanu'} ), #
			'avatar': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'avatar'}),			
            # 'avatar' : forms.FileInput(attrs={'class': 'form-control', 'name': 'avatar'}), #
            'locate_code' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Mã hộp đen', 'name': 'locate_code'}),
            'about_car' : forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Giới  thiệu',  'name': 'about_car'})

        }

# class ManuForm(object):
# 	"""docstring for ManuForm"""
# 	class Meta:
# 		model = ManuFacturers
# 		fields = ơ'name'ư
# 		label = Ơ
# 			'name' : 'Tên hãng'
# 		Ư
# 		widgets{
# 			'name' : forms.TextInput(attrs=Ơ'class': 'form-control','placeholder': 'Hãng Sản xuất xe', 'name': 'name'Ư),
# 		Ư
			
		
class DriverForm(ModelForm):
	"""docstring for Contacts"""
	class Meta:
		model = Driver
		fields = ['idcard', 'drivername', 'phone_number', 'address', 'birthday', 'experience','introduce', 'avatar']
		labels = {
			'drivername' : 'Tên tài xế',
			'idcard' : 'Chứng minh nhân dân',
			'avatar' : 'Ảnh đại diện',
			'phone_number' : 'Số điện thoại',
			'address' : 'Địa chỉ',
			'birthday' : 'Ngày, tháng, năm sinh',
			'experience' : 'Kinh nghiệm',
			'introduce' : 'Tiểu sử'
			
		}
		widgets = {
			'idcard': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nhập chứng minh nhân dân', 'name': 'idcard'}),
			'drivername': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên tài xế', 'name': 'drivername'}),
			# 'phone_number': widgets.PhoneNumberPrefixWidget(attrs={'class': 'form-control','placeholder': 'Nhập số điện thoại', 'name': 'phone_number'}),
			'phone_number' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Số điện thoại', 'name': 'phone_number'}),
			'address' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Địa chỉ thường trú', 'name': 'address'}),
			'birthday': forms.DateInput(attrs={'id':'datepicker', 'class': 'form-control','autocomplete':"off", 'name': 'birthday'}), #attrs={'class': 'form-control', 'name': 'age'}
            'experience' : forms.NumberInput(attrs={'class': 'form-control', 'name': 'experience'}), #attrs={'class': 'form-control', 'name': 'experience'}
			'introduce': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Giới  thiệu đôi chút về bản thân',  'name': 'introduce'}),
			'avatar': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'avatar'}),			

        }

class AlbumForm(ModelForm):  
	"""docstring for Contacts"""
	class Meta:
		model = Album
		fields = ['title','avatar', 'decription']
		labels = {
			'title' : 'Tên Album',
			'avatar': 'ảnh đại diện',
			'decription' : 'Mô tả'
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'title'}),
			'avatar': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control','placeholder': 'Tên album', 'name': 'avatar'}),			
			'decription': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Thêm mô tả',  'name': 'decription'}),
        }
class PhotoForm(ModelForm):
	"""docstring for Contacts"""
	class Meta:
		model = Photo
		fields = ['path_img', ]
		labels = {
			'path_img' : 'Đường dẫn',
			'comment_img' : 'Mô tả'
		}
		widgets = {
			# 'album': forms.TextInput(attrs={'readonly':'True','class': 'form-control','placeholder': 'Tên album', 'name': 'album'}),#ModelChoiceField(queryset= Album.objects.all()),
			'path_img': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control','placeholder': 'Tên album', 'name': 'path_img'}),			
			'comment_img': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Thêm mô tả',  'name': 'comment_img'}),
		}
PhotoFormset = modelformset_factory(
	Photo, 
	fields=('path_img', ),
	extra=1,
	labels = {
		'path_img' : 'Đường dẫn',
		},
	widgets = {
		'path_img': forms.ClearableFileInput(
			attrs={
			'class': 'form-control',
			'name': 'path_img'
			}
		)			
	}
)

class ScheduleForm(ModelForm):
	"""docstring for Contacts"""
	# car = forms.ModelMultipleChoiceField(queryset=Car.objects.all())
	class Meta:
		model = Schedule
		fields = ['departure_day', 'destination_day', 'departure', 'destination', 'departure_time', 'price', 'deposit', 'status']
		labels = {
			# 'car' : 'Loại Xe (Biển số)',
			'departure_day' : "Ngày khởi hành",
			'destination_day' : "Ngày về",
			'departure' : "Địa điểm khởi hành",
			'destination' : "Điểm đến",
			'departure_time' : "Thời gian xuất phát",
			'price' : "Giá",
			'deposit' : "Tiền cọc",
			'status' : "Trạng thái",
		}
		widgets = {
			# 'car': forms.Select(attrs={'class': 'form-control', 'name': 'car'}), #, attrs={'class': 'form-control','placeholder': 'Xe', 'name': 'car'}
			'departure_day': forms.DateInput(attrs={'id':'datepicker1','autocomplete':"off",'class': 'form-control','placeholder': 'Ngày khởi hành', 'name': 'departure_day'}),
			'destination_day': forms.DateInput(attrs={'id':'datepicker2','autocomplete':"off",'class': 'form-control','placeholder': 'Ngày về', 'name': 'destination_day'}),
            'departure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nơi khởi hành','name': 'departure'} ), #
            'destination' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Điểm đến cuối cùng', 'name': 'destination'}), #
            'departure_time': forms.TimeInput(attrs={'id':'timepicker1','autocomplete':"off", 'class': 'form-control','placeholder': 'Giờ khởi hành', 'name': 'departure_time'}),
			'price': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiền cho mướn xe', 'name': 'price'}),
            'deposit': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiền cọc', 'name': 'deposit'} ), #
            'status': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Trạng thái', 'name': 'status'} ), #
        }

class CostForm(ModelForm):
	"""docstring for Contacts"""
	class Meta:
		model = Cost
		fields = ['schedule', 'total_revenue', 'spent_oil', 'spent_steersman', 'spent_arises']
		labels = {
			'schedule' : 'Lịch trình',
			'total_revenue' : "Giá cho mướn xe",
			'spent_oil' : "Phí xăng dầu",
			'spent_steersman' : "Phí tài xế",
			'spent_arises' : "Các loại phí khác",
			
		}
		widgets = {
			'schedule': forms.Select(attrs={'class': 'form-control', 'name': 'schedule'}),
			'total_revenue': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiền cho thuê xe', 'name': 'total_revenue'}),
			'spent_oil': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Chi phí nhiên liệu (Tiền xăng dầu)', 'name': 'spent_oil'}),
			'spent_steersman' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Phí tài xế', 'name': 'spent_steersman'}),
			'spent_arises' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Phí phát sinh (tiền phạt, phí đường bộ...)', 'name': 'spent_arises'}),
			
        }

class UserLoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		label = {
			'username': 'Tên đăng nhập',
			'password': 'Mật khẩu',
		}
		widgets = {
			'username': forms.TextInput(attrs={'placeholder': 'Tài khoản đăng nhập','help_text': 'Vui lòng không bỏ trống', 'name': 'username'}),
			'password': forms.PasswordInput(attrs={'placeholder': 'Nhập mật khẩu', 'help_text': 'Vui lòng không bỏ trống', 'name': 'password'}),
			
        }
class UserRegisterForm(UserCreationForm):
	# confirm_password=forms.CharField(label=_("Nhập lại mật khẩu"), widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Nhập lại mật khẩu', 'name': 'confirm_password'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
		widgets = {
			'username': forms.TextInput(attrs={'placeholder': 'Tài khoản đăng nhập', 'name': 'username'}),
			'password1': forms.PasswordInput(attrs={'placeholder': 'Nhập mật khẩu', 'name': 'password1'}),
			'password2': forms.PasswordInput(attrs={'placeholder': 'Nhập lại mật khẩu', 'name': 'password2'}),
			# 'confirm_password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Nhập lại mật khẩu', 'name': 'confirm_password'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Nhập Tên', 'name': 'last_name'}),
			'first_name': forms.TextInput(attrs={'placeholder': 'Nhập Họ', 'name': 'first_name'}),
			# 'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Số điện thoại', 'name': 'phone'}),
			# 'permision': forms.Select(choices = permision_choose, attrs={'class': 'form-control', 'name': 'permision'}),
			
        }
  #   def clean(self):
		# cleaned_dât = super(UseregisterForm, self).clean()
  #       pasword = cleaned_data.get("pasword")
  #       confirm_pasword = cleaned_data.get("confirm_pasword")
  #       if pasword != confirm_pasword:
  #           raise forms.ValidationError("Mật khẩu nhập lại khồng khớp")
  #          
class ContentForm(ModelForm):
	class Meta:
		model = Content
		fields = ['avatar', 'title', 'slogan', 'phone','mobile', 'address', 'email', 'link', 'summary']
		labels = {
			'title' : "Tên dịch vụ",
			'slogan': "Slogan", 
			'avatar' : 'Ảnh đại diện',
			'phone' : "Số điện thoại",
			'mobile' : "Số di động",
			'address' : "Địa chỉ",
			'email' : "địa chỉ mail",
			'link' : "Các trang mạng liên kết",
			'summary': "Giớ thiệu công ty",
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên dịch vụ', 'name': 'title'}),
			'slogan': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Câu slogan cho dịch vụ', 'name': 'slogan'}),
			'avatar': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'avatar'}),
			'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Số điện thoại khách hàng', 'name': 'phone'}),
			'mobile': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Số điện thoại khách hàng', 'name': 'mobile'}),
			'email' : forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Nhâp địa chỉ mail', 'name': 'email'}),
			'address' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Địa chỉ liên hệ', 'name': 'address'}),
			'link': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Liên kế mạng xã hội', 'name': 'link'}),
			'summary': forms.Textarea(attrs={'id': 'content-blog', 'class': 'form-control','placeholder': 'Nội dung trang web', 'name': 'summary'}),
		}
class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'avatar', 'description']
		labels = {
			'name' : "Thể loại bài viết",
			'avatar': "Ảnh đại diện",
			'description' : "Diễn tả",
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control','placeholder': '', 'name': 'name'}),
			'avatar': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'avatar'}),			
			'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control','placeholder': 'Tiền cho thuê xe', 'name': 'description'}),
		}

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = ['category','title','avatar', 'content']
		labels = {
			'category' : "Thể loại",
			'title' : "Tiêu đề bài viết",
			'avatar': "Ảnh đại diện",
			'content' : "Nội dung",
		}
		widgets = {
			'category': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Thể loại tin', 'name': 'category'}),
			'avatar': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'avatar'}),	
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên dịch vụ', 'name': 'title'}),
			'content': forms.Textarea(attrs={'id': 'content-blog', 'name': 'content'}),
			# 'content': CKEditorWidget(),
		}

BlogFormset = modelformset_factory(
	Blog, 
	fields = ('title','avatar', 'content', ),
	extra=1,
	labels = {
		'title' : 'Tiêu đề',
		'avatar': "Ảnh đại diện",
		'content' : "Nội dung",
	},
	widgets = {
		'avatar': forms.ClearableFileInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Tên album', 
				'name': 'avatar'
			}),	
		'title': forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Tên dịch vụ', 
				'name': 'title'
			}),
		'content': forms.Textarea(
			attrs={
				'class': 'form-control',
				'id': 'content-blog', 
				'name': 'content'
		}),
				
	}
)

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['title', 'content']
		labels = {
			'title' : "Tiêu đề",
			'content' : "Bình luận",
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiêu đề bình luận', 'name': 'title'}),
			'content':  forms.Textarea(attrs={'class': 'form-control','placeholder': 'Nội dung bình luận', 'name': 'summary'}),
		}
		
class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['name', 'avatar', 'phone', 'address', 'cardid']
		labels = {
			'name' : "Họ tên",
			'avatar' : "Ảnh đại diện",
			'phone' : 'Số điện thoại',
			'address' : 'Địa chỉ',
			'cardid' : 'Chứng minh thư'
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Họ tên khách hàng', 'name': 'name'}),
			'avatar': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'avatar'}),			
			# 'avatar': forms.FileInput(attrs={'multiple': True, 'class': 'form-control','placeholder': 'Ảnh đại diện', 'name': 'avatar'}),
			'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Số điện thoại khách hàng', 'name': 'phone'}),
			'address': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Địa chỉ nhà', 'name': 'address'}),
			'cardid': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Số chứng minh nhân dân', 'name': 'cardid'}),
			
			
		}