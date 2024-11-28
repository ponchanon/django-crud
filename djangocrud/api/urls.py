from django.urls import path
from . import views


urlpatterns = [
    path('get', views.get_data, name='get_data'),
    path('add', views.add_data, name='add_data'),
]
