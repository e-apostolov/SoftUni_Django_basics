from django.urls import path, include

from cars.views import Catalogue, CarCreateView, CarDetailsView, CarEditView, CarDeleteView

urlpatterns = [
    path('catalogue/', Catalogue.as_view(), name='catalogue'),
    path('create/', CarCreateView.as_view(), name='create-car'),
    path('<int:id>/', include([
        path('details/', CarDetailsView.as_view(), name='car-details'),
        path('edit/', CarEditView.as_view(), name='car-edit'),
        path('delete/', CarDeleteView.as_view(), name='car-delete'),
    ]))
]


