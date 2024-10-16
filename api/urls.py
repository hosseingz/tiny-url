from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('c/', views.CreateAPIView.as_view(), name='create_short_link'),
    path('t/<str:q>', views.TinyAPIView.as_view(), name='redireckt_url')
]
