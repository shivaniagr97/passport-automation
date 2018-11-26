from django.contrib import admin
from .models import profile, userStripe,Details,Documents,Verified

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile,profileAdmin)

class userStripeAdmin(admin.ModelAdmin):
	class Meta:
		model = userStripe

admin.site.register(userStripe,userStripeAdmin)

class detailsAdmin(admin.ModelAdmin):
	class Meta:
		model = Details

admin.site.register(Details,detailsAdmin)

class documentsAdmin(admin.ModelAdmin):
	class Meta:
		model = Documents

admin.site.register(Documents,documentsAdmin)

class verification(admin.ModelAdmin):
	class Meta :
		model = Verified
admin.site.register(Verified,verification)	

