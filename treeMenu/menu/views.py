from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class ListMenu(ListView):
    model = Menu
    context_object_name = 'menu_list'

    template_name = 'menu/menu.html'


class DetailMenu(DetailView):
    model = List
    context_object_name = 'list'
    template_name = 'menu/detail.html'
