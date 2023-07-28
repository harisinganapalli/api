from rest_framework import serializers
from .models import Fruits

class Fruits_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Fruits
        fields=['id','name','description']
        

        #httpie
        #curl
        #crud operations api 
        