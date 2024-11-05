from rest_framework import serializers
from .models import Country

# Tento serializátor převádí instanci Country na JSON a naopak

class CountrySerializer(serializers.ModelSerializer):        
    class Meta:
        model = Country
        fields = ['id', 'name', 'country_code', 'created_at', 'group_id']  
                                                        
class CountryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'country_code'] 