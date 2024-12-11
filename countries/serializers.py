from rest_framework import serializers
from .models import Country
from .countries_by_continent import list_by_continent


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


class CountryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'country_code']

    def validate_country_code(self, value):
        valid_codes = [code for countries in list_by_continent.values() for code in countries.values()]
        if value not in valid_codes:
            raise serializers.ValidationError(f"Invalid country code: {value}")
        return value


        