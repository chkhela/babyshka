from django.urls import path, include
from. import views

urlpatterns = [
    path('',views.index),
    path('page1',views.page),
    path('page2',views.page2),
    path('page3',views.page3),
    path('page4',views.page4),
    path('page5',views.page5),
    path('page6',views.page6),
    path('page7',views.page7),
    path('page8',views.page8),
    path('page20',views.page20),
]