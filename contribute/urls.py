from django.urls import path

from .views import (
    contribute
)

app_name = 'contribute'

urlpatterns = [
    path('', contribute, name='contribute'),
]