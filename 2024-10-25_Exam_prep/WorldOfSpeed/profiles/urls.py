from django.urls import path, include

from profiles.views import CreateProfileView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('', CreateProfileView.as_view(), name='create_profile'),
    path('<int:id>/', include([
        path('details/', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]