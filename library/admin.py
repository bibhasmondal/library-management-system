from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Book)
admin.site.register(Subject)
admin.site.register(Request)
admin.site.register(New)