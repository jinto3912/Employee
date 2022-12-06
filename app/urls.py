
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('add',views.create),
    path('show',views.read),
    path('del',views.delete),
    path('up',views.update),

]