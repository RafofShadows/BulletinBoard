from django.urls import path

from .views import BulletinListAll

urlpatterns = [
    path('', BulletinListAll.as_view(), name='bulletins_all'),

]