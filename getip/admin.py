from django.contrib import admin

from .models import Author

class AuthorInfoAdmin(admin.ModelAdmin):
	list_display=('id','first_name','last_name','email')

admin.site.register(Author,AuthorInfoAdmin)