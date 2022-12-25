from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

Tank = 'TA'
Heal = 'HE'
DD = 'DD'
Merchant = 'ME'
Guildmaster = 'GM'
Questgiver = 'QG'
Smith = 'BM'
Tanner = 'LW'
Alchemist = 'AL'
Caster = 'SM'
CATEGORY = [
    (Tank, 'Танки'),
    (Heal, 'Хилы'),
    (DD, 'ДД'),
    (Merchant, 'Торговцы'),
    (Guildmaster, 'Гилдмастеры'),
    (Questgiver, 'Квестгиверы'),
    (Smith, 'Кузнецы'),
    (Tanner, 'Кожевники'),
    (Alchemist, 'Зельевары'),
    (Caster, 'Мастера заклинаний')
]


# Create your models here.
class Bulletin(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100, default='')
    body = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=2, choices=CATEGORY, default='DD')


class Response(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
