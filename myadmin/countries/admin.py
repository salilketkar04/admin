from django.contrib import admin

# Register your models here.
from countries.models import Countries

admin.site.register(Countries)