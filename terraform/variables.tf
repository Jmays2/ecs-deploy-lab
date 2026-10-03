variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name used for AWS resources"
  type        = string
  default     = "ecs-deploy-lab"
}

variable "github_repository" {
  description = "GitHub repository in OWNER/REPO format"
  type        = string
  default     = "Jmays2/ecs-deploy-lab"
}
