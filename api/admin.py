from django.contrib import admin
# from .models import User, UserCode, Users
from .models import UserData, Code

# Register your models here.
# admin.site.register([User, UserCode,  Users])

admin.site.register([UserData, Code])
