from .views import product_list, product_detail, product_create, product_update, product_delete
from django.urls import path

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('<str:product_name>/', product_detail, name='product_detail'),
    path('<str:product_name>/update/', product_update, name='product_update'),
    path('<str:product_name>/delete/', product_delete, name='product_delete'),
]