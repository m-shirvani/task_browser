resource "aws_cloudwatch_log_group" "task_browser-log-group" {
  name              = "/ecs/task_browser-app"
  retention_in_days = var.log_retention_in_days
}

resource "aws_cloudwatch_log_stream" "task_browser-log-stream" {
  name           = "task_browser-app-log-stream"
  log_group_name = aws_cloudwatch_log_group.task_browser-log-group.name
}

