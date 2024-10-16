from rest_framework import serializers
from .models import Url



class UrlSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Url
            fields = ['url', 'short_link', 'created']
            
        extra_kwargs = {
            'url': {'write_only': True},
        }