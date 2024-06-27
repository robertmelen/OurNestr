from django.urls import path
from . import views
from .views import CustomLogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<int:pk>', views.dashboard, name='dashboard'),
    path('houseform/', views.houseform, name='houseform'),
    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('delete/', views.delete_house, name='delete_house'),
    path('edithouse/<int:pk>', views.edit_house, name='edit_house'),
    path('filter/', views.house_filter, name='house_filter')
   

]