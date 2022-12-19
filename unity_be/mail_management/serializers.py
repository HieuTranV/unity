from rest_framework import serializers
from .models import Partner, Mail

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__" 


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"