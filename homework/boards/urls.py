from django.urls import path
from .views import BoardView, BoardListView

app_name = "boards"

urlpatterns = [
    path('', BoardListView.as_view(), name='board-list'),
    path('<int:pk>', BoardView.as_view(), name='board-detail'),
]