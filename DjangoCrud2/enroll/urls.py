from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_display, name='addandshow'),
    path('del/<int:id>/', views.delete, name='delete'),

]
