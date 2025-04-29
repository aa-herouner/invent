from django.urls import path

from .views import (
    create_buyer,
    create_category,
    create_product,
    create_order,
    edit_product,
    product_list,
    get_product_price,
    get_order_list,
    # dashboard_order_list,
    BuyerListView,
    CategoryListView,
    # OrderListView,
)


urlpatterns = [
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-drop/', create_category, name='create-category'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('edit-product/<int:pk>', edit_product, name='edit-product'),
    path('product-list/', product_list, name='product-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('drop-list/', CategoryListView.as_view(), name='category-list'),
    path('order-list/',get_order_list, name='order-list'),
    path('get-product-price/', get_product_price, name='get-product-price'),
    # path('dashboard/', dashboard_order_list, name='dashboard-order-list'),
]