from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework import generics, views
from django.shortcuts import redirect
from .serializers import *
from .models import Url


class CreateAPIView(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Url.objects.all()
    
    serializer_class = UrlSerializer
        
        

class TinyAPIView(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    
    def get(self, request, q):
        
        obj = get_object_or_404(Url, short_link=q)
        
        return redirect(obj.url)
