from django.contrib import admin

from .models import Allip

class AllInfoAdmin(admin.ModelAdmin):
	list_display=('id','all_ip')

admin.site.register(Allip,AllInfoAdmin)