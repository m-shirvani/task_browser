import logging
import uuid
from django.db import models
from django.utils import timezone


logger = logging.getLogger(__name__)


class Tasks(models.Model):
    class TaskStatusChoices(models.TextChoices):
        SCHEDULED = "SC", "Scheduled"
        RUNNING = "R", "Running"
        COMPLETED = "C", "Completed"
        IDLE = "I", "Idle"
        MULTI_RUN = "M", "Multi-Run"

    class Meta:
        verbose_name_plural = "Tasks"

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    parent = models.ForeignKey("Tasks", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def is_node(self):
        return False if self.tasks_set.exists() else True

    @property
    def get_node_status(self):
        now = timezone.now()
        if self.start_date > now:
            return self.TaskStatusChoices.SCHEDULED.label
        if self.start_date < now < self.end_date:
            return self.TaskStatusChoices.RUNNING.label
        if self.end_date < now:
            return self.TaskStatusChoices.COMPLETED.label

    @property
    def scheduled_subtasks(self):
        now = timezone.now()
        return self.tasks_set.filter(start_date__gt=now)

    @property
    def running_subtasks(self):
        now = timezone.now()
        return self.tasks_set.filter(start_date__lte=now, end_date__gt=now)

    @property
    def is_multi_run(self):
        return True if self.running_subtasks.count() > 1 else False

    @property
    def completed_subtasks(self):
        now = timezone.now()
        return self.tasks_set.filter(start_date__lte=now, end_date__lt=now)

    @property
    def get_task_status(self):
        if self.is_node:
            return self.get_node_status
        else:
            if self.scheduled_subtasks and not self.running_subtasks:
                return self.TaskStatusChoices.SCHEDULED.label
            if self.running_subtasks and not self.is_multi_run:
                return self.TaskStatusChoices.RUNNING.label
            if self.is_multi_run:
                return self.TaskStatusChoices.MULTI_RUN.label
            if (
                self.completed_subtasks
                and self.scheduled_subtasks
                and not self.running_subtasks
            ):
                return self.TaskStatusChoices.IDLE.label
            else:
                return self.TaskStatusChoices.COMPLETED.label
