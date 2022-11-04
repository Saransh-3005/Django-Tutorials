from msilib.schema import Feature
from django.contrib import admin
from .models import Feature
from .models import Blog
# Register your models here.
admin.site.register(Feature)
admin.site.register(Blog)