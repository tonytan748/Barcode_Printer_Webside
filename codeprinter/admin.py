from django.contrib import admin

# Register your models here.

from .models import *

class WebInfoAdmin(admin.ModelAdmin):
	class Meta:
		model=WebInfo

class ClassifyAdmin(admin.ModelAdmin):
	class Meta:
		model=Classify

class CompanyAdmin(admin.ModelAdmin):
	class Meta:
		model=Company

class ProductAdmin(admin.ModelAdmin):
	class Meta:
		model=Product

admin.site.register(WebInfo,WebInfoAdmin)
admin.site.register(Classify,ClassifyAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Product,ProductAdmin)
