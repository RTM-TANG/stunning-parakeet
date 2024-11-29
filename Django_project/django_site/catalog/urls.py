from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /catalog/1/detail/
    path("<int:item_id>/", views.detail, name="detail"),
    # ex: /catalog/1/price/
    path("<int:item_id>/price/", views.price, name="price"),
    # ex: /catalog/1/stock/
    path("<int:stock_id>/stock/", views.stock_check, name="stock"),
    
    path("add/", views.commission_create, name = 'commission-create')
]