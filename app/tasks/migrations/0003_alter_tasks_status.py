# Generated by Django 3.2 on 2021-04-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tasks_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('SC', 'Scheduled'), ('R', 'Running'), ('C', 'Completed'), ('I', 'Idle'), ('M', 'Multi-Run')], default='SC', max_length=2),
        ),
    ]
