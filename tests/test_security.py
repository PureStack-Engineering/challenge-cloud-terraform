import hcl2
import pytest
import os

# Leemos el archivo main.tf
with open("terraform/main.tf", "r") as file:
    tf_code = hcl2.load(file)

def test_s3_bucket_is_private():
    """Level 1: S3 Buckets must be private."""
    # Buscamos el recurso aws_s3_bucket
    buckets = tf_code.get("resource", [])[0].get("aws_s3_bucket", {})
    
    for name, config in buckets.items():
        acl = config.get("acl", "private")
        assert acl == "private", f"🚨 SECURITY ALERT: Bucket '{name}' has ACL '{acl}'. Must be 'private'."

def test_security_group_no_open_ssh():
    """Level 2: Port 22 (SSH) must NOT be open to 0.0.0.0/0."""
    sgs = tf_code.get("resource", [])[1].get("aws_security_group", {})
    
    for name, config in sgs.items():
        ingress_rules = config.get("ingress", [])
        for rule in ingress_rules:
            from_port = int(rule.get("from_port"))
            to_port = int(rule.get("to_port"))
            cidr = rule.get("cidr_blocks", [])
            
            # Si es el puerto 22, NO puede tener 0.0.0.0/0
            if from_port <= 22 <= to_port:
                assert "0.0.0.0/0" not in cidr, f"🚨 SECURITY ALERT: Security Group '{name}' has Port 22 open to the world!"
