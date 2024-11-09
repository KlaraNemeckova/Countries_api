from rest_framework import serializers
from .models import Country


# Serializer for retrieving and viewing country data
class CountrySerializer(serializers.ModelSerializer):        
    class Meta:
        model = Country
        # Fields to include in the serialized output for API responses
        fields = ['id', 'name', 'country_code', 'created_at', 'group_id']  

# Serializer for creating a new country record                                                  
class CountryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        # Fields needed for creating a country record (excluding auto-generated fields)
        fields = ['name', 'country_code'] 


        