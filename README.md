# ☁️ PureStack Infrastructure Challenge: The Terraform Guardrails

**PureStack.es - Engineering Validation Protocol.**
> *"Infrastructure is code. And code must be secure by design."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol for Cloud Engineering.
We don't verify if you can click buttons in the AWS Console. We audit your ability to write **Secure Infrastructure as Code (IaC)**.

**The Scenario:** A junior developer has committed a Terraform file (`terraform/main.tf`) to provision resources for a finance application.
**The Problem:** The code is functional but **extremely insecure**. It violates critical compliance policies.
**The Mission:** You must act as the **Security Engineer**. Audit the code, run the policy checks, and refactor the Terraform to make it secure without breaking the infrastructure.

### 🚦 Certification Levels (Choose your Difficulty)
State your target level in your Pull Request.

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Basic Security Hygiene.
* **Requirement:** Fix the critical vulnerabilities to pass the provided security tests.
* **Tasks:**
    1.  **S3 Audit:** The bucket `finance_data` is publicly accessible. Change the ACL to `private`.
    2.  **Network Audit:** The Security Group `web_sg` allows SSH (Port 22) from `0.0.0.0/0` (The entire internet). Restrict it to a specific CIDR (e.g., `10.0.0.0/8` or a VPN IP) or remove the rule entirely.
* **Deliverable:** The security tests (`pytest`) must return GREEN.

#### 🥈 Level 2: Pro / Senior
* **Focus:** Best Practices & Encryption.
* **Requirement:** Everything in Level 3 + **Encryption & Variables**.
* **Extra Tasks:**
    1.  **Encryption:** Financial data must be encrypted at rest. Add a `server_side_encryption_configuration` block to the S3 bucket using `AES256`.
    2.  **No Hardcoding:** The bucket name and CIDR blocks are hardcoded. Refactor them into `variables.tf` and use `var.bucket_name` in the main file.
* **Deliverable:** Secure, encrypted, and reusable Terraform code.

#### 🥇 Level 1: Elite / Architect
* **Focus:** Policy as Code (PaC) & Modularity.
* **Requirement:** Everything above + **Custom Policy**.
* **Extra Tasks:**
    1.  **New Security Rule:** We need to ensure Versioning is enabled.
        * **Terraform:** Enable `versioning` on the S3 bucket.
        * **Python Test:** Add a NEW test function in `tests/test_security.py` that parses the HCL and asserts that `versioning { enabled = true }` is present.
    2.  **Output:** Ensure the secure bucket ARN is exported in `outputs.tf`.
* **Deliverable:** You don't just follow rules; you write the rules that others follow.

---

### 🛠️ Tech Stack & Constraints
* **Language:** HCL (Terraform).
* **Validation Tool:** Python (`pytest` + `python-hcl2`) acts as the "Policy Engine".
* **Cloud Provider:** AWS (Mocked - No real credentials needed).

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Audit the Code:**
    * Run the security scanner: `pytest tests/`
    * Observe the 🚨 Security Alerts.
4.  **Fix the Vulnerabilities:**
    * Edit `terraform/main.tf`.
    * Re-run `pytest` until all tests pass.
5.  Submit via **Pull Request**.

> **Note:** You will see a ❌ (**Red Cross**) initially. This is the security scanner blocking the insecure deployment. Your goal is to turn it ✅ (**Green**).

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Security** | 40% | Did you close the public bucket and the open SSH port? |
| **Best Practices** | 30% | usage of `variables.tf` vs Hardcoding (Level 2). |
| **Code Quality** | 20% | Correct HCL syntax and formatting (`terraform fmt`). |
| **Tooling** | 10% | Ability to write/modify Python tests (Level 1). |

---

### 🚨 Project Structure (Strict)
To ensure our **Automated Auditor** works, keep the core structure:

```text
/
├── .github/workflows/   # PureStack Audit System
├── terraform/
│   ├── main.tf          # <--- VULNERABLE CODE HERE
│   ├── variables.tf
│   └── outputs.tf
├── tests/
│   └── test_security.py # <--- THE SECURITY POLICE (Python Script)
├── .gitignore
├── requirements.txt     # Dependencies
└── README.md
