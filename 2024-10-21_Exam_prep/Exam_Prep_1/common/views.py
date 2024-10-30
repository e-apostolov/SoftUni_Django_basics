from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from Exam_Prep_1.utils import get_user_obj
from albums.models import Album
from profiles.forms import ProfileCreateForm


class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_obj() # Returns None or QuerySet

        if profile:
            return ['common/home-with-profile.html']

        return ['common/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)