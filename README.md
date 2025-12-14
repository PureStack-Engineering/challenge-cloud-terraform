# ☁️ PureStack Cloud Challenge: The Terraform Protocol

PureStack.es Cloud. Validated by Code.

### Context
Welcome to the **PureStack Technical Validation Protocol** for Cloud Engineering.
Infrastructure is no longer about clicking buttons in the AWS Console. It's about code, reproducibility, and security compliance.

**⚠️ The Scenario:** We need to provision a secure web server environment on AWS.
**Constraint:** You must use **Terraform** (or OpenTofu). Do NOT assume we have CLI access; your code must work from a clean slate.

---

### 🎯 The Objective
Write the Terraform code in `main.tf` to define the following infrastructure:

1.  **VPC:** CIDR `10.0.0.0/16`.
2.  **Subnet:** Public Subnet with CIDR `10.0.1.0/24`.
3.  **Security Group:**
    * Allow Inbound **HTTP (80)** and **HTTPS (443)** from anywhere (`0.0.0.0/0`).
    * **CRITICAL:** Do NOT open SSH (22) to the world.
4.  **EC2 Instance:**
    * AMI: `ami-0c55b159cbfafe1f0` (Ubuntu standard mock).
    * Type: `t2.micro`.
    * Network: Must be placed in the created Subnet and attached to the Security Group.

### 🛠️ Tech Stack Requirements
* **Tool:** Terraform 1.5+ or OpenTofu.
* **Provider:** AWS (`hashicorp/aws`).
* **Style:** HCL (HashiCorp Configuration Language).

## 🧪 Evaluation Criteria (How we audit you)

We will run a static analysis on your code. We look for:

- **Syntax Validity:** `terraform validate` must pass.
- **Resource Completeness:** Did you define `aws_vpc`, `aws_subnet`, `aws_instance`, and `aws_security_group`?
- **Security Check:** We check if port 22 is exposed to `0.0.0.0/0` (Fail condition).

## 🚀 Getting Started

1. Use this template.
2. Initialize locally: `terraform init`.
3. Write the resources in `main.tf`.
4. Validate locally: `terraform validate`.
5. Submit via Pull Request.

---

### 🚨 CRITICAL: Project Structure
To ensure our **Automated Auditor** works, keep the file structure simple:

```text
/
├── .github/workflows/   # PureStack Audit System
│   └── audit.yml    
├── main.tf              # <--- YOUR CODE GOES HERE (Single file is fine for this test)
├── .gitignore
└── README.md
