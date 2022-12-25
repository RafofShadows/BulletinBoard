from django.shortcuts import render
from django.views.generic import ListView

from .filters import BulletinFilterCategory
from .models import Response, Bulletin


# Create your views here.


class BulletinListAll(ListView):
    model = Bulletin
    ordering = '-timestamp'
    template_name = 'bulletins.html'
    context_object_name = 'bulletins'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BulletinFilterCategory(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


