from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^add_item", views.CreateItemView.as_view(), name="add_inventory_item"),
    re_path(r"^items/", views.ListItemView.as_view(), name="list_inventory_item"),
    re_path(r"^item/buy", views.BuyItemView.as_view(), name="buy_inventory_item"),
]