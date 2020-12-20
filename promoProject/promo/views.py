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
    include default used methods 
    '''
    def list(self,request):
        '''
        if super user:
            retrieve list of promo objects 
            retrieve single promo object and remaing points if promo object exists
        if normal user:
            retrieve list of promo objects related to user 
            retrieve single promo object and remaing points if promo object exists and related to user 

        '''
        serializer=self.get_serializer_class();
        user=request.user;
        q=request.GET.get('q',None);
        pk=request.GET.get('pk',None);
        if not(user.is_superuser):
            queryset=self.get_queryset().filter(user=user);
            if pk==None:
                 serializer=serializer(queryset,many=True);
                 return Response(serializer.data);
            elif pk !=None:
                  queryset=get_object_or_404(queryset,pk=pk);
                  if q == None:
                      serializer=serializer(queryset);
                      return Response(serializer.data);
                  else:
                       if hasattr(queryset,'amount'):
                           return Response({"Remainig Points":queryset.amount});
                       else:
                           return Response({"Remainig Points":None});
        else:
            queryset=self.get_queryset();
            if pk==None:
                serializer=serializer(self.get_queryset(),many=True);
                return Response(serializer.data);
            if pk != None:
                   
                   queryset=get_object_or_404(queryset,pk=pk);
                   
                   if q != None:
                       if hasattr(queryset,'amount'):
                           
                           return Response({"Remainig Points":queryset.amount});
                   
                   serializer=serializer(queryset);
                   return Response(serializer.data); 
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
    def get_permissions(self):
        '''
        handle permissions dynamically according to request method 
        '''
        method=self.request.method;
        admin_methods=['PUT','POST','DELETE']
        if method in admin_methods:
            return (IsAuthenticated(),IsAdminUser(),)
        elif method=='GET' or method=='OPTIONS':
            
            return (IsAuthenticated(),)
        elif method=='PATCH':
            return (IsAuthenticated(),isForNormalUser(),)
        else:
            return (IsAuthenticated(),)