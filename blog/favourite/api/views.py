from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from favourite.models import Favourite

from .paginations import FavouritePagination
from .serializers import (FavouriteAPISerializer,
                          FavouriteCreateListAPISerializer)
                
from .permissions import IsOwner


class FavouriteCreateListAPIView(ListCreateAPIView):
    serializer_class = FavouriteCreateListAPISerializer
    pagination_class = FavouritePagination
    permission_classes = IsAuthenticated
    
    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'pk'
    permission_classes =[IsOwner]
