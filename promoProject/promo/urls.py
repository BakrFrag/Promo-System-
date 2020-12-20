from .views import *;
from django.urls import path;
from rest_framework.urlpatterns import format_suffix_patterns
promo_list=PromoViewSet.as_view({
    "get":"list",
});
promo_create=PromoViewSet.as_view({
    "post":"create",
});
promo_update=PromoViewSet.as_view({
    "put":"update",
});
promo_delete=PromoViewSet.as_view({
    'delete': 'destroy',
});
promo_partial_update=PromoViewSet.as_view({
    "patch":'partial_update'
});

urlpatterns = format_suffix_patterns([
path('list/',promo_list,name="promo_list"),
path('create/',promo_create,name="create_promo"),
path('delete/<int:pk>/',promo_delete,name="delete_promo"),
path('update/<int:pk>/',promo_update,name="update_promo"),
path('update/<int:pk>/amount/',promo_partial_update,name="promo_partial_update")
]);

