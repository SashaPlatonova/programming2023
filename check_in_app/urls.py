from rest_framework import routers
from django.urls import path, include
from check_in_app import views
from .views import *


app_name = "check_in_app"


urlpatterns = [
    path('residents/all', ResidentList.as_view()),
    path('residents/create', ResidentCreateView.as_view()),
    path('residents/update/<int:pk>/', ResidentUpdate.as_view()),
    path('residents/all/<int:pk>/', ResidentRetrive.as_view()),
    path('types/all', views.TransportTypeListView.as_view()),
    path('types/all/<int:pk>/', TypeRetrive.as_view()),
    path('transport/all', views.TransportListView.as_view()),
    path('transport/all/<int:pk>/', TransportRetrive.as_view()),
    path('transport/create', TransportCreateView.as_view()),
    path('transport/delete/<int:pk>/', TransportDelete.as_view()),
    path('order/all', OrderListView.as_view()),
    path('order/filter/busy', OrderSetFilteredByDateBusyView.as_view()),
    path('transport/filter/free', TransportSetFilteredByDateFreeView.as_view()),
    path('transport/filter/busy', TransportSetFilteredByDateBusyView.as_view()),
    path('transport/filter/params', TransportFindByParamsView.as_view()),
    path('order/create', OrderCreateView.as_view()),
    ]
