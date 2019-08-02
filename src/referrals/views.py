from django.shortcuts import render
from rest_framework import viewsets
from .models import Referral, PageView
from .serializers import ReferralSerializer


class ReferralView(viewsets.ModelViewSet):
    """ All CRUD actions performed by using the ModelViewSet module """
    queryset = Referral.objects.all()  # specifies how to get the objects from the database
    serializer_class = ReferralSerializer


def home(request):
    referrals = Referral.objects.all()
    return render(request, 'home.html', {'referrals': referrals})


def landing_page(request, pk):
    referral = Referral.objects.get(pk=pk)
    if PageView.objects.count() <= 0:
        x = PageView.objects.create()
        x.save()
    else:
        x = PageView.objects.all()[0]
        x.hits += 1
        x.save()
    print(x.hits)
    return render(request, 'landing.html', {'referral': referral})


