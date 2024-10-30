from django.views.generic import TemplateView

from posts.models import Post


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'
