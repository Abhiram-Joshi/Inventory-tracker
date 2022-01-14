from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import ItemSerializer
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