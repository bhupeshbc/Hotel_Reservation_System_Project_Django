from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("allRooms",views.allRooms, name= 'allRooms')
]
urlpatterns += staticfiles_urlpatterns()
