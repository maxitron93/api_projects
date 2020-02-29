from django.urls import path
from .views import (TaskListCreateAPIView,
                    BookDetailAPIView)

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='tasks_list'),
    path('<int:pk>', BookDetailAPIView.as_view(), name='task_details')
]