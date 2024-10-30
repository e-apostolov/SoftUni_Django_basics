from django.urls import path

from common.views import Index
from posts.views import Dashboard

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]