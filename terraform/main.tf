provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "finance_data" {
  bucket = "purestack-finance-logs"
  acl    = "public-read"  # 🚨 FALLO 1: Bucket público

  tags = {
    Environment = "Dev"
  }
}

resource "aws_security_group" "web_sg" {
  name        = "web_server_sg"
  description = "Allow inbound traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # HTTP OK
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # 🚨 FALLO 2: SSH abierto a todo el mundo
  }
}
