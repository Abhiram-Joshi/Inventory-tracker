from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CreateItemView(CreateAPIView):
    serializer_class = ItemSerializer

class ListItemView(ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "data": serializer.data,
            "message": "Items retrieved successfully",
            "status": status.HTTP_200_OK,
        }, status=status.HTTP_200_OK)

class BuyItemView(UpdateAPIView):
    serializer_class = BuyItemSerializer

    def get_queryset(self):
        return Item.objects.all()

    def get_object(self):
        item = self.get_queryset().filter(id=self.request.query_params["id"])
        return item

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        instance = item[0]
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        if(instance.quantity>=serializer.validated_data["quantity"]):
            instance.quantity -= serializer.validated_data["quantity"]
            instance.save()
            return Response({
                "data": item.values()[0],
                "message": "Item bought",
                "status": status.HTTP_200_OK,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "data": [],
                "message": "Not enough quantity available",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)

class DeleteItemView(DestroyAPIView):

    def get_queryset(self):
        return Item.objects.all()

    def get_object(self):
        item = self.get_queryset().filter(id=self.request.query_params["id"])
        return item

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        if item.exists():
            name = item[0].name
            item.first().delete()
            return Response({
                "data": name,
                "message": "Item removed",
                "status": status.HTTP_200_OK,
            }, status = status.HTTP_200_OK)
        else:
            return Response({
                "data": [],
                "message": "Item could not be removed",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_404_NOT_FOUND)