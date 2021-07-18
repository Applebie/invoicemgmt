from django.urls import path
from . import views 

#UrlConf - every app can have its own url config
urlpatterns = [path('clients/', views.show_client_details )]