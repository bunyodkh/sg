from django.urls import path

from space.views import main_space, startup_support_program

app_name = 'space'

urlpatterns = [
    path('', main_space, name='main-space'),
    path('startup-support-program/', startup_support_program, name='startup-support-program'),
]