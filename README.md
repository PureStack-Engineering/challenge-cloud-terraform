# ☁️ PureStack Cloud Challenge: The Terraform Protocol

**PureStack.es - Cloud Infrastructure Validation.**
> *"Infrastructure is not about clicking buttons. It's about Code, State, and Security."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol for Cloud Engineering.
We audit your ability to define reproducible, secure infrastructure using **Terraform (IaC)**. We don't want "ClickOps"; we want code that can be audited and versioned.

**The Mission:** Provision a secure web server environment on AWS.
**The Constraint:** Do NOT assume CLI access or existing resources. Your code must work from a clean slate (`terraform init` -> `terraform apply`).

### 🚦 Certification Levels (Choose your Difficulty)
Your seniority is defined by how you structure your code, manage state, and modularize resources. State your target level in your Pull Request.

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Resource Definition & Syntax.
* **Requirement:** Define the core infrastructure in `main.tf`.
* **Tasks:**
    1.  **VPC:** Create a Virtual Private Cloud (`10.0.0.0/16`).
    2.  **Subnet:** Create a Public Subnet (`10.0.1.0/24`) inside the VPC.
    3.  **Security Group:**
        * Allow **HTTP (80)** and **HTTPS (443)** from anywhere (`0.0.0.0/0`).
        * **CRITICAL:** Do NOT open SSH (22) to the world. (Restrict to a specific IP or close it).
    4.  **EC2:** Provision a `t2.micro` instance (Ubuntu AMI) attached to the Subnet and Security Group.
* **Deliverable:** Valid HCL code that passes `terraform validate`.

#### 🥈 Level 2: Pro / Senior
* **Focus:** Reusability, Variables & Outputs.
* **Requirement:** Everything in Level 3 + **No Magic Strings**.
* **Extra Tasks:**
    1.  **Variables:** Do not hardcode CIDRs, AMI IDs, or Instance Types. Use `variables.tf` with default values or a `.tfvars` file.
    2.  **Outputs:** Create an `outputs.tf` file that prints the **Public IP** of the created instance after deployment.
    3.  **Tagging Strategy:** Apply a consistent tag (e.g., `Project = "PureStack"`, `Environment = "Dev"`) to ALL resources automatically.
* **Deliverable:** A clean, parameterized configuration separating logic from data.

#### 🥇 Level 1: Elite / Architect
* **Focus:** Modules, Provisioning & State Management.
* **Requirement:** Everything above + **Modularization & User Data**.
* **Extra Tasks:**
    1.  **Refactoring (Modules):** Move the Networking logic (VPC, Subnet, Gateway) into a reusable `./modules/network` folder. Call this module from the root `main.tf`.
    2.  **Bootstrapping:** Use `user_data` to install an actual web server (Nginx/Apache) upon boot, creating a simple "Hello PureStack" `index.html`.
    3.  **Architecture Diagram:** Include a text-based diagram or Mermaid code in the PR description explaining the flow.
* **Deliverable:** A scalable, modular infrastructure ready for team collaboration.

---

### 🛠️ Tech Stack Requirements
* **Tool:** Terraform 1.5+ or OpenTofu.
* **Provider:** AWS (`hashicorp/aws`).
* **Style:** HCL (HashiCorp Configuration Language).
* **Linter:** `tflint` (Recommended locally).

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Initialize locally: `terraform init`.
3.  Write your resources in `main.tf` (or split files for Level 2/1).
4.  Validate syntax: `terraform validate`.
5.  Submit via **Pull Request** stating your target Level.

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Security** | 35% | Is Port 22 open to the world? (Immediate Fail). Are permissions least-privilege? |
| **Syntax & Style** | 25% | Formatting (`terraform fmt`), valid references. |
| **Best Practices** | 25% | Usage of variables vs hardcoding. Tagging. |
| **Modularity** | 15% | Directory structure and module usage (Level 1). |

---

### 🚨 Project Structure (Guideline)
To ensure our **Automated Auditor** works, keep the entry point clear.

**Standard Structure (Level 2/1 Recommended):**
```text
/
├── .github/workflows/   # PureStack Audit System (DO NOT TOUCH)
├── modules/             # <--- (Optional) For Level 1
│   └── network/
├── main.tf              # <--- ENTRY POINT
├── variables.tf         # <--- DEFINITIONS
├── outputs.tf           # <--- RESULTS
├── .gitignore
└── README.md
