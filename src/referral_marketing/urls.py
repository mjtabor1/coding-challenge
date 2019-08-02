from django.contrib import admin
from django.conf.urls import url
from referrals import views
from django.urls import include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^referrals/(?P<pk>\d+)/$', views.landing_page, name='landing_page'),
    url('api/', include('referrals.urls')),
]


