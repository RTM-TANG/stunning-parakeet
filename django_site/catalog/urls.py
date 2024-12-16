""" Lists all urls path in the django application """

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /catalog/1/detail/
    path("<int:item_id>/", views.detail, name="detail"),
    # ex: /catalog/1/stock/
    path("<int:commission_id>/commission/", views.info_commission, name="commission-detail"),
    path("<int:stock_id>/stock/", views.stock_check, name="stock"),
    path("add/", views.commission_create, name = 'commission-create')
]