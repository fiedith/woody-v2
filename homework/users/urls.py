from django.urls import path

from .views import UserView, UserDeleteView

app_name = 'users'

urlpatterns = [
    path('', UserView.as_view(), name='user-api'),
    path('<int:pk>', UserDeleteView.as_view(), name='user-api'),
]