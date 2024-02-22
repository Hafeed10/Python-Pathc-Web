from django.urls import path
from pathc2.views import index, subscribe

app_name = 'pathc2'

urlpatterns = [
    path("", index, name="pathc2"),          
    path('pathc2/', index, name='pathc2'),
    path("subscribe/", subscribe, name="subscribe"), 
]
