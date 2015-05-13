from django.contrib import admin

from .models import check_all_ip

class check_all_ipInfoAdmin(admin.ModelAdmin):
	list_display=('id','ip','test_ip')

admin.site.register(check_all_ip,check_all_ipInfoAdmin)