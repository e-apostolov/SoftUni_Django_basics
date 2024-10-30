from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FurryFunnies.utils import get_user_obj
from authors.forms import AuthorCreateForm, AuthorEditForm
from authors.models import Author
from posts.models import Post


class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object
        posts = author.posts.all()

        last_updated_post = posts.order_by('updated_at').last()
        context['total_posts'] = posts.count()
        # context['last_updated_post'] = last_updated_post if last_updated_post else "N/A"
        context['last_updated_post'] = last_updated_post

        return context

class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        return get_user_obj()

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()
