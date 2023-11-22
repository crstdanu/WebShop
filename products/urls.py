from django.urls import path
from . import views
# will import the views  module from our folder NO MATTER where our folder is


# /products
#
urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]
