[
  {
    "name": "task_browser-app",
    "image": "${docker_image_url_task_browser}",
    "essential": true,
    "cpu": 10,
    "memory": 512,
    "links": [],
    "portMappings": [
      {
        "containerPort": 8000,
        "hostPort": 0,
        "protocol": "tcp"
      }
    ],
    "command": ["gunicorn", "-w", "3", "-b", ":8000", "task_browser.wsgi:application"],
    "environment": [],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/task_browser-app",
        "awslogs-region": "${region}",
        "awslogs-stream-prefix": "task_browser-app-log-stream"
      }
    }
  }
]
