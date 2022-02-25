from django.contrib import admin

# Register your models here.

from .models import Student , Collage, Principal , Dpartment, Subject 

admin.site.register([Student, Collage, Principal, Dpartment , Subject])
