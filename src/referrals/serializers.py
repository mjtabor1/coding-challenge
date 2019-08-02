from rest_framework import serializers
from .models import Referral


class ReferralSerializer(serializers.ModelSerializer):
    """ Serializer that will show the information relevant to the model.
    Can create new models and update existing ones."""

    class Meta:
        model = Referral  # model that represents the Referral class
        fields = ('id', 'name', 'url')  # fields to display in the API
