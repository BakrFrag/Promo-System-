from django.db import models
from django.contrib.auth.models import User;
class AdminManager(models.Manager):
    '''
    custom manager to handle superusers
    '''
    def get_queryset(self):
         return super(AdminManager,self).get_queryset().filter(is_superuser=True);
class NormalManager(models.Manager):
    '''
    custom manager to handle normal users
    '''
    def get_queryset(self):
          return super(NormalManager,self).get_queryset().filter(is_superuser=False);
class AdminUser(User):
    objects=AdminManager();
    class Meta:
        proxy=True;
class NormalUser(User):
    objects=NormalManager();
    class Meta:
        proxy=True;