provider "aws" {
  region = "us-east-1"
}

# 🚨 SECURITY VIOLATION 1: Public Bucket
resource "aws_s3_bucket" "finance_data" {
  bucket = "purestack-finance-logs-2024"
  acl    = "public-read" # <--- CANDIDATE MUST FIX THIS

  tags = {
    Environment = "Production"
    Department  = "Finance"
  }
}

# 🚨 SECURITY VIOLATION 2: Open SSH
resource "aws_security_group" "web_sg" {
  name        = "web-server-sg"
  description = "Security group for web server"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # <--- CANDIDATE MUST FIX THIS
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
