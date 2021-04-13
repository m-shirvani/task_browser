# Generated by Django 3.2 on 2021-04-13 10:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('SCHEDULED', 'SCHEDULED'), ('RUNNING', 'RUNNING'), ('COMPLETED', 'COMPLETED'), ('IDLE', 'IDLE'), ('MULTIRUN', 'MULTIRUN')], max_length=50)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
