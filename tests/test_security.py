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
    resources = tf_code.get('resource', [])
    found = False

    for entry in resources:
        # Check if this resource block is an s3 bucket
        if 'aws_s3_bucket' in entry:
            # entry['aws_s3_bucket'] is a dict of {name: config}
            buckets = entry['aws_s3_bucket']
            for name, config in buckets.items():
                if name == 'finance_data':
                    found = True
                    acl = config.get('acl', 'private')
                    assert acl == 'private', f"🚨 SECURITY ALERT: Bucket '{name}' is '{acl}'. Must be 'private'."

    if not found:
        pytest.fail("❌ Resource 'aws_s3_bucket.finance_data' not found in main.tf")

def test_ssh_is_restricted(tf_code):
    """
    Policy: SSH (Port 22) must NOT be open to the world (0.0.0.0/0).
    """
    resources = tf_code.get('resource', [])
    
    for entry in resources:
        if 'aws_security_group' in entry:
            security_groups = entry['aws_security_group']
            for name, config in security_groups.items():
                
                # Normalize ingress rules (can be a list or single dict)
                ingress_rules = config.get('ingress', [])
                if isinstance(ingress_rules, dict):
                    ingress_rules = [ingress_rules]
                
                for rule in ingress_rules:
                    # Check from_port (can be int or string in parsed HCL)
                    from_port = int(rule.get('from_port', 0))
                    
                    if from_port == 22:
                        cidrs = rule.get('cidr_blocks', [])
                        assert "0.0.0.0/0" not in cidrs, \
                            f"🚨 SECURITY ALERT: Security Group '{name}' allows SSH from 0.0.0.0/0. Restrict it!"
