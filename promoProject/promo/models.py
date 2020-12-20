from django.db import models
from django.contrib.auth.models import User;
from .helpers import getPromoCode ,now;
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
Promo_Types=(("Percentage",'percentage'),('Points','points'))
class Promo(models.Model):
    kind=models.CharField(max_length=256,choices=Promo_Types,default='points')
    code=models.CharField(max_length=100,editable=False,default=getPromoCode);
    created=models.DateTimeField(auto_now_add=True);
    start=models.DateTimeField()
    end=models.DateTimeField();
    amount=models.PositiveIntegerField(validators=[MinValueValidator(1)]);
    user=models.ForeignKey(NormalUser,on_delete=models.CASCADE);
    @property
    def is_active(self):
        now=datetime.now(timezone.utc);
        print(now >= self.start)
        if now >= self.start and now<=self.end:
            return True;
        return False;