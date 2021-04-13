import django_tables2 as tables
from django_tables2 import SingleTableView

from .models import Tasks


class TasksTable(tables.Table):
    class Meta:
        model = Tasks
        template_name = "django_tables2/bootstrap.html"
        fields = (
            "uuid",
            "name",
            "get_task_status",
            "start_date",
            "end_date",
            "parent",
            "is_node",
        )


class TasksListView(SingleTableView):
    model = Tasks
    table_class = TasksTable
    template_name = "home.html"
