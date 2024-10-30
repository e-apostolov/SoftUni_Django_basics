from django.urls import path

from authors.views import CreateAuthorView, AuthorDetailView, AuthorEditView, AuthorDeleteView

urlpatterns = [
    path('create/', CreateAuthorView.as_view(), name='create-author'),
    path('details/', AuthorDetailView.as_view(), name='details-author'),
    path('edit/', AuthorEditView.as_view(), name='edit-author'),
    path('delete/', AuthorDeleteView.as_view(), name='delete-author'),
]