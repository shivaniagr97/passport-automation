from django.contrib import admin
from .models import RegAdmin,Dates,DocsVerified,VStatus
# Register your models here.

class RegAdminclass(admin.ModelAdmin):
	class Meta:
		model = RegAdmin

admin.site.register(RegAdmin,RegAdminclass)

class Datesclass(admin.ModelAdmin):
	class Meta:
		model = Dates

admin.site.register(Dates,Datesclass)


class veriStatus(admin.ModelAdmin):
	class Meta :
		model = VStatus
admin.site.register(VStatus , veriStatus)		

class verification(admin.ModelAdmin):
	class Meta :
		model = DocsVerified
admin.site.register(DocsVerified,verification)		