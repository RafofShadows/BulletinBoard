from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .filters import BulletinFilterCategory
from .forms import BulletinForm
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


class BulletinDetail(DetailView):
    model = Bulletin
    template_name = 'bulletin.html'
    context_object_name = 'bulletin'


class BulletinCreate(CreateView):
    form_class = BulletinForm
    model = Bulletin
    template_name = 'bulletin_edit.html'

    def form_valid(self, form):
        bulletin = form.save(commit=False)
        super().form_valid(form)
        return redirect('board/')



