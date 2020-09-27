from django.urls import path
from .views import FavouriteCreateListAPIView, FavouriteAPIView

app_name = "favourite"

urlpatterns = [
    path('list-create', FavouriteCreateListAPIView.as_view(), name='list-create'),
    path('update-delete/<pk>', FavouriteAPIView.as_view(), name='update-delete'),
]
