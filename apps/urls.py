from django.urls import path

from apps.views import add_user

urlpatterns = [
    path('post',add_user,name='add')
]

