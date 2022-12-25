from django.urls import path

from .views import BulletinListAll, BulletinDetail, BulletinCreate

urlpatterns = [
    path('', BulletinListAll.as_view(), name='bulletins_all'),
    path('bulletin/<int:pk>', BulletinDetail.as_view(), name='bulletin_detail'),
    path('bulletin/create/', BulletinCreate.as_view(), name='bulletin_create'),

]