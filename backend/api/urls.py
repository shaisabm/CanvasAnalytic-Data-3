from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/register/', CreateUserView.as_view(), name='register'),
    path('note/', CreateNoteView.as_view(), name='note'),

]
