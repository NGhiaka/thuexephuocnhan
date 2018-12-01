from django.contrib.auth.models import User
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
# Create user and save to the database
user = User.objects.create_user('admin', 'nhankn@gmail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'Nhân'
user.last_name = 'Lê'
user.save()