from django_filters import FilterSet, CharFilter, ChoiceFilter

from .models import CATEGORY


class BulletinFilterCategory(FilterSet):
    #category = CharFilter(field_name='category', lookup_expr='iexact', label='Категория')
    category = ChoiceFilter(choices=CATEGORY, label='Категория')

    class Meta:
        fields = {
            'category',
        }
