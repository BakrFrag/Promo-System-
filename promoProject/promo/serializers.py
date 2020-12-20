from rest_framework import serializers;
from rest_framework.exceptions import APIException;
from .models import *;
      
class promoListSerializer(serializers.ModelSerializer):
    '''
    used to list or serialize list of promo objects 
    active handle status of promo 
    '''
    active=serializers.BooleanField(source='is_active',read_only=True);
    class Meta:
        model=Promo;
        fields=['pk','code','kind','created','active','start','end','amount','user'];