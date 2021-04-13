from ariadne.contrib.django.views import GraphQLView
from django.contrib import admin
from django.urls import path

from tasks.views import TasksListView
from tasks.resolver import schema

urlpatterns = [
    path('', TasksListView.as_view(), name='home'),
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]