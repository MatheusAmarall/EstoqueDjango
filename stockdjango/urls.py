from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search-product/', views.search_product, name='search-product'),
    path('out-stock/', views.out_stock, name='out-stock'),
    path('add-product/', views.add_product, name='add-product'),
    path('product-detail/<int:id>', views.product_detail, name='product-detail'),
    path('delete-product/<int:id>', views.delete_product, name='delete-product'),
    path('sell-product/<int:id>', views.sell_product, name='sell-product'),
    path('user-logout/', views.user_logout, name='user-logout'),
]