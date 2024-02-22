from django.urls import path
from pathc2.views import index, subscribe

app_name = 'pathc2'

urlpatterns = [
    path("", index, name="pathc2"),          # Maps the root URL to the index view
    path('pathc2/', index, name='pathc2'),   # Maps '/pathc2/' URL to the index view
    path("subscribe/", subscribe, name="subscribe"),  # Maps '/subscribe/' URL to the subscribe view
]
