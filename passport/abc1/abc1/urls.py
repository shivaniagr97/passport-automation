"""abc1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from profiles import views as profile_views
from contact import views as contact_views
from checkout import views as checkout_views
from Admins import views as admin_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profile_views.home, name='home'),
    url(r'^about/$', profile_views.about, name='about'),
    url(r'^profile/$', profile_views.userProfile, name='profile'),
    url(r'^dashboard/$', profile_views.dashboard, name='dashboard'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^thank_you/$', checkout_views.charge, name='checkout'),
    url(r'^Applicant_Form/2/payment/$', checkout_views.checkout, name='checkout'),
    url(r'^admin_login/$', admin_views.admin_login, name='admin_p'),
    url(r'^admin_home/$', admin_views.admin_home, name='admin_home'),
    url(r'^admin_verify/$', admin_views.verify_app, name='admin_verify'),
    url(r'^admin_verify/2/', admin_views.verify_docs, name='admin_verify_docs'),
    url(r'^select_date/$', admin_views.dashboard, name='admin_dashboard'),
    url(r'^police/$', profile_views.police, name='police'),
    url(r'^police/test/$', profile_views.test, name='police_test'),
    url(r'^police/test/validate/$', profile_views.validate, name='police_test_validate'),
    url(r'^Applicant_Form/$', profile_views.product_create_view, name='user_form'),
    url(r'^Applicant_Form/2/$', profile_views.documents_view, name='user_form_2'),
    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    #urlpatterns += staticfiles_urlpatterns()

