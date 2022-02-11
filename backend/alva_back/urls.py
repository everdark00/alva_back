from django.urls import path
from django_filters.views import FilterView
from .views import *

urlpatterns = [
    path('create/', ProductCreate.as_view()),
    path('products/', ProductListAll.as_view()),
    path('cats/', ProductListCats.as_view()),
    path('sale/', ProductListSale.as_view()),
    path('new_col/', ProductListNew.as_view()),
    path('drop/<int:pk>', ProductListDelete.as_view()),
    path('product/<int:pk>', GetProduct.as_view()),
    path('orders/', OrderListAll.as_view()),
    path('create_order/', OrderCreate.as_view()),
    path('drop_order/<int:pk>', OrderListDelete.as_view()),
]