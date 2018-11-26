
from django.contrib import admin
from .models import user_payment
# Register your models here.

class paymentAdmin(admin.ModelAdmin):
	class Meta:
		model = user_payment

admin.site.register(user_payment,paymentAdmin)

