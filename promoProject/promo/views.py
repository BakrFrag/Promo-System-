from django.shortcuts import render
from django.shortcuts import render,get_object_or_404;
from rest_framework.viewsets import ModelViewSet;
from rest_framework import generics,status;
from .permissions import *;
from .models import *;
from .serializers import *;
from rest_framework.permissions import IsAdminUser,IsAuthenticated;
from rest_framework.response import Response;
from rest_framework.validators import ValidationError;
class PromoViewSet(ModelViewSet):
    '''
    '''
    def get_serializer_class(self):
        '''
        handle serializer dynamically acording to request action
        '''
        action=self.action;
        if action=='list' or action=='retrieve':
            return promoListSerializer;
        elif action=='create'or action=='update':
            return promoSerializer
        elif action=='partial_update':
            return promoPartialSerializer;