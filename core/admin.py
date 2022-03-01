from django.contrib import admin

from core.models import Resume
from . models import Resume
@admin.register(Resume)
class UserModeladmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','email','mobile','locality','city','state','pin','job_city','profile_image','my_file']
# Register your models here.
