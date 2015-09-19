from rest_framework import viewsets
from inventory.models import Item
from inventory.serializer import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()