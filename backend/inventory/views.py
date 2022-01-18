from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
# Create your views here.

class CreateItemView(CreateAPIView):
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "data": response.data,
            "message": "Item created successfully",
            "status": status.HTTP_200_OK,
        }, status = status.HTTP_200_OK)

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
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()

    def get_object(self):
        item = self.get_queryset().filter(id=self.request.query_params["id"])
        return item

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        if item.exists():
            data = self.get_serializer(item.first()).data
            item.first().delete()
            return Response({
                "data": data,
                "message": "Item removed",
                "status": status.HTTP_200_OK,
            }, status = status.HTTP_200_OK)
        else:
            return Response({
                "data": [],
                "message": "Item not found",
                "status": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_404_NOT_FOUND)

class CreateShipmentView(CreateAPIView):
    serializer_class = CreateShipmentSerializer

    def create(self, request, *args, **kwargs):
        item = Item.objects.get(id=request.data["item"])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if item.quantity >= serializer.validated_data["quantity"]:
            item.quantity -= serializer.validated_data["quantity"]
            item.save()
            response = super().create(request, *args, **kwargs)
            return Response({
                "data": response.data,
                "message": "Shipment created successfully",
                "status": status.HTTP_200_OK,
            }, status = status.HTTP_200_OK)
        
        else:
            return Response({
                "data": [],
                "message": "Not enough quantity available",
                "status": status.HTTP_400_BAD_REQUEST,
            }, status = status.HTTP_400_BAD_REQUEST)

class ShipmentDeliveredView(UpdateAPIView):

    def get_queryset(self):
        return Shipment.objects.all()

    def get_object(self):
        shipment = self.get_queryset().filter(id=self.request.query_params["id"])
        return shipment

    def update(self, request, *args, **kwargs):
        shipment = self.get_object()
        instance = shipment[0]
        if instance.cancelled:
            return Response({
                "data": shipment.values()[0],
                "message": "Shipment cancelled, cannot be delivered",
                "status": status.HTTP_400_BAD_REQUEST,
            }, status=status.HTTP_400_BAD_REQUEST)

        if instance.delivered:
            instance.delivered = True
            instance.save()
            return Response({
                "data": shipment.values()[0],
                "message": "Shipment already delivered",
                "status": status.HTTP_400_BAD_REQUEST,
            }, status=status.HTTP_400_BAD_REQUEST)

        else:
            instance.delivered = True
            instance.save()
            return Response({
                "data": shipment.values()[0],
                "message": "Shipment delivered",
                "status": status.HTTP_200_OK,
            }, status=status.HTTP_200_OK)

class ShipmentCancelledView(UpdateAPIView):
    
        def get_queryset(self):
            return Shipment.objects.all()
    
        def get_object(self):
            shipment = self.get_queryset().filter(id=self.request.query_params["id"])
            return shipment
    
        def update(self, request, *args, **kwargs):
            shipment = self.get_object()
            instance = shipment[0]

            if instance.delivered:
                return Response({
                    "data": [],
                    "message": "Shipment already delivered, cannot be cancelled",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)

            if instance.cancelled:
                return Response({
                    "data": [],
                    "message": "Shipment already cancelled",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)

            else:
                item = Item.objects.get(id=instance.item.id)
                item.quantity += instance.quantity
                item.save()
                instance.cancelled = True
                instance.save()
                return Response({
                    "data": shipment.values()[0],
                    "message": "Shipment cancelled",
                    "status": status.HTTP_200_OK,
                }, status=status.HTTP_200_OK)

class ListShipmentView(ListAPIView):
    serializer_class = ShipmentSerializer

    def get_queryset(self):
        return Shipment.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "data": serializer.data,
            "message": "Shipments retrieved successfully",
            "status": status.HTTP_200_OK,
        }, status=status.HTTP_200_OK)