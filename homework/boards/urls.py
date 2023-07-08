from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BoardView, BoardListView, CommentViewSet

app_name = "boards"

router = DefaultRouter()
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', BoardListView.as_view(), name='board-list'),
    path('<int:pk>', BoardView.as_view(), name='board-detail'),

    # endpoint: /api/boards/comments/
    path('', include(router.urls))
]