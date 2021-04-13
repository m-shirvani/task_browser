from django.contrib import admin
from django.urls import path, include

from tasks.views import TasksListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TasksListView.as_view()),
]