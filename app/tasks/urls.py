from ariadne.contrib.django.views import GraphQLView
from django.contrib import admin
from django.urls import path, include

from tasks.views import TasksListView

from tasks.resolver import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TasksListView.as_view()),
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]