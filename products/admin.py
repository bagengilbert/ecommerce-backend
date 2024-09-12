from django.contrib import admin
from .models import product, Categoty

# Register your models here.
#register and category models with the admin site to manage them by django admin interface 

admin.site.register(product)
admin.site.register(Categoty)
