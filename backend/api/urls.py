
from django.urls import path, include
from .views import *

urlpatterns = [
    path('sampledata/', GetSampleData.as_view(), name='get_sample_data')
]
