from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from favourite.models import Favourite


class FavouriteCreateListAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite

        fields = '__all__'

    #to avoid creating the same record again
    def validate(self, attrs):
        queryset = Favourite.objects.filter(post=attrs["post"], user=attrs["user"])
        
        if queryset.exists():
            raise serializers.ValidationError("Already added to favorites!")
        return attrs


class FavouriteAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite

        fields = ['content']

 