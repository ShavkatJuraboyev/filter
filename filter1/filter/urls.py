from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_list, name="index"),
    path('django/', views.person_list1, name="django"),
    path('export_word/', views.export_users_to_word, name='export_word'),
    path('export_excel/', views.export_users_to_excel, name='export_excel'),
]