from django.urls import path

from .views import *

urlpatterns = [
    path('', ListMenu.as_view(), name='menu'),
    path('<int:pk>', DetailMenu.as_view(), name='detail')
]
