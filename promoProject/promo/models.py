from django.db import models
from django.contrib.auth.models import User;
class AdminManager(models.Manager):
    def get_queryset(self):
         return super(AdminManager,self).get_queryset().filter(is_superuser=True);