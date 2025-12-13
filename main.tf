terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  # Note: No credentials needed for 'terraform validate'
}

# -----------------------------------------------------------
# 1. DEFINE VPC
# -----------------------------------------------------------
# TODO: Create aws_vpc resource


# -----------------------------------------------------------
# 2. DEFINE SUBNET
# -----------------------------------------------------------
# TODO: Create aws_subnet resource


# -----------------------------------------------------------
# 3. DEFINE SECURITY GROUP (Web Traffic Only)
# -----------------------------------------------------------
# TODO: Create aws_security_group resource


# -----------------------------------------------------------
# 4. DEFINE EC2 INSTANCE
# -----------------------------------------------------------
# TODO: Create aws_instance resource linked to the Subnet and SG
