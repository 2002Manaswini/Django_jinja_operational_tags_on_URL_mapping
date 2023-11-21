from django.urls import path
from specific.views import *

app_name='something'

urlpatterns=[
    path('bapi/',bapi,name='bapi'),
    path('babul/',babul,name='babul'),
]