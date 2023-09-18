from django.urls import path
from msafiri import views

urlpatterns = [
     path('', views.index, name='index'),
     path('add_car/', views.add_car, name='add_car'),
     path('add_car/', views.add_car, name='add_car'),
     path('add_car/insert_car/', views.insert_car, name='insert_car'),
     path('routes/', views.routes, name='routes'),
     path('about_us/', views.about_us, name='about_us'),
     path('add_route/', views.add_route, name='add_route'),
     path('add_route/insert_route/', views.insert_route, name='insert_route'),
     path('add_company/', views.add_company, name='add_company'),
     path('add_company/insert_company/', views.insert_company, name='insert_company'),
     path('add_route/edit_route/<int:id>', views.edit_route, name='edit_route'),
     path('add_route/delete_route/<int:id>', views.delete_route, name='delete_route'),
     path('add_car/delete_car/<int:id>', views.delete_car, name='delete_car'),
     path('add_company/delete_company/<int:id>', views.delete_company, name='delete_company'),
     path('add_region/', views.add_region, name='add_region'),
     path('add_region/insert_region/', views.insert_region, name='insert_region'),
     path('add_region/delete_region/<int:id>', views.delete_region, name='delete_region'),
     path('add_region/update_region/<int:id>', views.update_region, name='update_region'),
]