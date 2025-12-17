import hcl2
import pytest
import os

TERRAFORM_FILE = "terraform/main.tf"

@pytest.fixture
def tf_code():
    """Parses the main.tf file into a Python Dict"""
    if not os.path.exists(TERRAFORM_FILE):
        pytest.fail(f"❌ File not found: {TERRAFORM_FILE}")
    
    with open(TERRAFORM_FILE, 'r') as file:
        return hcl2.load(file)

def test_s3_is_private(tf_code):
    """
    Policy: S3 Buckets must NOT be public.
    Check: acl must be 'private'.
    """
    # Navigate the HCL structure: resource -> aws_s3_bucket -> finance_data
    resources = tf_code.get('resource', [])
    s3_buckets = [r for r in resources if 'aws_s3_bucket' in r]
    
    found = False
    for bucket_wrapper in s3_buckets:
        for name, config in bucket_wrapper.items():
            if name == 'finance_data':
                found = True
                acl = config.get('acl', 'private') # Default if missing
                assert acl == 'private', f"🚨 SECURITY ALERT: Bucket '{name}' is '{acl}'. Must be 'private'."
    
    if not found:
        pytest.fail("❌ Resource 'aws_s3_bucket.finance_data' not found. Do not delete it, fix it!")

def test_ssh_is_restricted(tf_code):
    """
    Policy: SSH (Port 22) must NOT be open to the world (0.0.0.0/0).
    """
    resources = tf_code.get('resource', [])
    security_groups = [r for r in resources if 'aws_security_group' in r]
    
    for sg_wrapper in security_groups:
        for name, config in sg_wrapper.items():
            ingress_rules = config.get('ingress', [])
            # In HCL2 parsing, ingress might be a list of dicts
            if isinstance(ingress_rules, dict):
                ingress_rules = [ingress_rules]
            
            for rule in ingress_rules:
                from_port = int(rule.get('from_port', 0))
                cidrs = rule.get('cidr_blocks', [])
                
                # Check for Port 22
                if from_port == 22:
                    assert "0.0.0.0/0" not in cidrs, \
                        f"🚨 SECURITY ALERT: Security Group '{name}' allows SSH from 0.0.0.0/0. Restrict it!"
