# Generated by Django 2.1 on 2018-11-29 22:35

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to='album/%Y/%m/%d')),
                ('decription', models.CharField(blank=True, max_length=200)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to='blog/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
                ('dateSubmit', models.DateField(default=datetime.date.today, verbose_name='date published')),
                ('view', models.IntegerField(default=0)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carid', models.CharField(max_length=50)),
                ('nameofcar', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('typecar', models.CharField(max_length=15)),
                ('yearofmanu', models.CharField(max_length=15)),
                ('avatar', models.ImageField(blank=True, default='/static/images/uploads/default/car.jpg', upload_to='avatar/%Y/%m/%d')),
                ('locate_code', models.CharField(default='', max_length=50)),
                ('about_car', models.CharField(max_length=1000)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('avatar', models.ImageField(upload_to='category/%Y/%m/%d')),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=5000)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='/static/images/uploads/default/car.jpg', upload_to='avatar/%Y/%m/%d')),
                ('title', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Số điện thoại phải có định dạng 0xxxxxxxxxxx.', regex='^\\0\\d{8,15}$')])),
                ('slogan', models.CharField(blank=True, max_length=2000)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(default='nhanknth@gmail.com', max_length=254)),
                ('link', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('spent_oil', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('spent_steersman', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('spent_arises', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, default='/static/images/uploads/default/user.png', upload_to='avatar/%Y/%m/%d')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Số điện thoại phải có định dạng 0xxxxxxxxxxx.', regex='^[0-9]{8,15}$')])),
                ('address', models.CharField(blank=True, max_length=100)),
                ('cardid', models.CharField(blank=True, max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcard', models.CharField(max_length=10)),
                ('drivername', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('introduce', models.CharField(max_length=1000)),
                ('birthday', models.DateField()),
                ('experience', models.IntegerField()),
                ('avatar', models.ImageField(default='/static/images/uploads/default/user.png', null=True, upload_to='avatar/%Y/%m/%d')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Số điện thoại phải có định dạng 0xxxxxxxxxxx.', regex='^[0-9]{8,15}$')])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_img', models.ImageField(upload_to='travel/%Y/%m/%d')),
                ('comment_img', models.CharField(max_length=200)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.Album')),
            ],
        ),
        migrations.CreateModel(
            name='RandomID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_day', models.DateField(verbose_name='date published')),
                ('destination_day', models.DateField(verbose_name='date published')),
                ('departure', models.CharField(max_length=500)),
                ('destination', models.CharField(max_length=500)),
                ('departure_time', models.TimeField(verbose_name='date published')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.Car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='cost',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.Schedule'),
        ),
        migrations.AddField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.Customer'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.Category'),
        ),
    ]
