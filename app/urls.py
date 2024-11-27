# from django.urls import path
# from app.views import About,Home,Contact,Login,Logout_admin

# urlpatterns=[
#     path('',Home,name='home'),
#     path('about/',About,name='about'),
#     path('contact/',Contact,name='contact'),
#     path('admin_login/',Login,name='admin_login'),
#     path('logout/',Logout_admin,name='logout_admin'),
# ]

# urls.py
from django.urls import path
from app.views import * 

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('adminpage/',AdminPage,name='adminpage'),

    # STADIUM
    path('add_stadium/', add_stadium, name='add_stadium'),
    path('update_stadium/', update_stadium, name='update_stadium'),
    path('delete_stadium/<int:id>/', delete_stadium, name='delete_stadium'),
    #EQUIPMENT
    path('add_equipment/',add_equipment,name='add_equipment'),
    path('update_equipment/',update_equipment,name='update_equipment'),
    path('delete_equipment/<int:id>/',delete_equipment,name='delete_equipment'),

    #CUSTOMER
    path('add_customer/', add_customer, name='add_customer'),
    path('update_customer/', update_customer, name='update_customer'),
    path('delete_customer/<int:id>/', delete_customer, name='delete_customer'),


    path('user_login/', UserLogin, name='user_login'), 
    path('user_logout/', Logout_user, name='logout_user'), 
    path('register/', registerPage, name='register'),  
    
    path('stadium_list/', stadium_list, name='stadium_list'),
    path('equipment_list/', equipment_list, name='equipment_list'),
    path('customer_list/', customer_list, name='customer_list'),


]