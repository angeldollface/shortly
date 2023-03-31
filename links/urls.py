# SHORTLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

from .views import link
from .views import error
from .views import add_link
from django.urls import path
from .views import redirect_to

app_name = 'links'

urlpatterns = [
    path('', add_link, name='home'),
    path('<int:pk>/', link, name='link'),
    path('<str:err>', error, name='error'),
    path('<int:pk>/run', redirect_to, name='redirect_to'),
]