from django.urls import path

from common.views import Index

urlpatterns = [
    path('', Index.as_view(), name='home'),
]