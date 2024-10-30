from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from WorldOfSpeed.utils import get_user_obj
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object
        cars = profile.cars.all()
        total_price = sum(car.price for car in cars)
        context['total_price'] = total_price
        return context

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/profile-edit.html'
    pk_url_kwarg = 'id'
    def get_success_url(self):
        profile_id = self.object.id
        return reverse_lazy('profile-details', kwargs={'id': profile_id})


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()





