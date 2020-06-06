from django.urls import path

from . import views

urlpatterns = [
    path('contact', views.my_seventh),
    path('delivery', views.my_sixth),
    path('service', views.my_fifth),
    path('store', views.my_fourth),
    path('repair', views.my_third),
    path('rent', views.my_second),
    path('', views.my_first),
]
