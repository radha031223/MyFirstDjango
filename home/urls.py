from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
     #path("is the name of the page, that will be added after the ip", view.function ka naam which is made in views.py, name="name which will be useful for linking the buttons in html")
    

    path('', views.index, name='Home'),
    path('Contact-Us/', views.contact, name='Contact us'),  # Avoid spaces in URL paths
    path('Home/', views.index, name='IndexTemp'),
    path('About-Us/', views.about, name='about us'),       # Avoid spaces in URL paths
    path('My-List/', views.mylist, name='list'),
    path('Login/', views.login, name='login'),
    path('Sign-up/', views.signup, name='signup'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('list/<int:list_id>/', views.list_detail, name='list_detail'),
    path('create_list/', views.create_list, name='create_list'),
    path('list/<int:list_id>/add_item', views.add_item, name='add_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),

]



