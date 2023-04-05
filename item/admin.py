from django.contrib import admin

# Register your models here.
from .models import CategoryModel,Item

admin.site.register([CategoryModel,Item])