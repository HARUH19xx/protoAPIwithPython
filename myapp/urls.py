from django.urls import path
from . import views

urlpatterns = [
    path('api/data/', views.get_data, name='get_data'),
]
