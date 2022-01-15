from django.urls import re_path
from . import views

urlpatterns = [
    # Inventory item CRUD
    re_path(r"^add_item", views.CreateItemView.as_view(), name="add_inventory_item"),
    re_path(r"^items/", views.ListItemView.as_view(), name="list_inventory_item"),
    re_path(r"^item/buy", views.BuyItemView.as_view(), name="buy_inventory_item"),
    re_path(r"^item/delete", views.DeleteItemView.as_view(), name="delete_inventory_item"),

    # Shipment CRUD
    re_path(r"^create_shipment", views.CreateShipmentView.as_view(), name="create_shipment"),
    re_path(r"^shipment/delivered", views.ShipmentDeliveredView.as_view(), name="shipment_delivered"),
    re_path(r"^shipment/cancel", views.ShipmentCancelledView.as_view(), name="shipment_cancel"),
    re_path(r"^shipments/", views.ListShipmentView.as_view(), name="list_shipment"),
]