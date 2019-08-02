from django.urls import path, include
from . import views
from rest_framework import routers


# router takes care of generating all of the URLS for the model
router = routers.DefaultRouter()
router.register('referrals', views.ReferralView)


urlpatterns = [
    path('', include(router.urls)),
]
