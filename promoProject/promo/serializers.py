from rest_framework import serializers;
from rest_framework.exceptions import APIException;
from .models import *;
      
class promoListSerializer(serializers.ModelSerializer):
    '''
    used to list or serialize list of promo objects or promo object
    active handle status of promo 
    '''
    active=serializers.BooleanField(source='is_active',read_only=True);
    class Meta:
        model=Promo;
        fields=['pk','code','kind','created','active','start','end','amount','user'];
class promoSerializer(serializers.ModelSerializer):
    '''
    used to create/update promo objects and validate objects 
    promo start date or end date can't be in past
    promo end date can't be less than promo start date 
    promo of type percentage amount can't exceed 100
    '''
    class Meta:
        model=Promo;
        fields=['kind','start','end','amount','user'];
    def create(self, validated_data):
        return Promo(**validated_data)
    def validate(self,data):
        start=data['start'];
        end=data['end'];
        kind=data['kind'];
        amount=data['amount']
        now=datetime.now(timezone.utc);
        if start < now:
            raise ValidationError("promo start time must be in present not in past")
        if start > end:
            raise ValidationError("promo start date must be less than promo end date")
        if end < now:
            raise ValidationError("promo end date must be in futur not in present or past")
                  
        if kind=='Percentage' and (amount > 100 or amount < 0):
            raise ValidationError("promo of kind percentage amount must be greather than zero and less than or equal 100");
        return data;