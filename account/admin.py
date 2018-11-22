from django.contrib import admin
from .models import *

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_filter = ('Year_Of_Passing','Department')

admin.site.register(Student, StudentAdmin)
