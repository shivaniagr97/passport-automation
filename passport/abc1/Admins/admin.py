from django.contrib import admin
from .models import RegAdmin,Dates
# Register your models here.

class RegAdminclass(admin.ModelAdmin):
	class Meta:
		model = RegAdmin

admin.site.register(RegAdmin,RegAdminclass)

class Datesclass(admin.ModelAdmin):
	class Meta:
		model = Dates

admin.site.register(Dates,Datesclass)
