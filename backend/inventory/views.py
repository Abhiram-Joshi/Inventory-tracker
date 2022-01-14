from rest_framework.generics import CreateAPIView
from .serializers import ItemSerializer
# Create your views here.

class CreateItemView(CreateAPIView):
    serializer_class = ItemSerializer