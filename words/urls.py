from django.urls import path
from .views import *

app_name = 'words'

urlpatterns = [
    path('', letters_input, name='letters')
]