from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^add_item", views.CreateItemView.as_view(), name="add_inventory_item"),
]