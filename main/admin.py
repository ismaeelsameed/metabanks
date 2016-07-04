from django.contrib import admin

# Register your models here.
from main.models import News, Contact

admin.site.register(News)
admin.site.register(Contact)
