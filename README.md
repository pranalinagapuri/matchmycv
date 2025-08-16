# AWS EC2 Deployment with Terraform + NGINX

This project uses **Terraform** to provision an **AWS EC2 instance** running **NGINX** on Amazon Linux 2.  
It's designed as an Infrastructure-as-Code (IaC) example with a clean, reusable configuration and **GitHub Actions CI** for Terraform validation.

---

## 📂 Project Structure

```plaintext
├── main.tf                  # Main Terraform configuration
├── variables.tf             # Input variables
├── outputs.tf               # Outputs after deployment
├── ec2_install.sh           # EC2 user data script to install & configure NGINX
├── index.html               # Default HTML landing page
├── .gitignore               # Files ignored by Git
├── terraform.tfvars.example # Example variable file (no secrets)
└── .github/
    └── workflows/
        └── ci.yml           # GitHub Actions Terraform validation
```

---

## ✅ Prerequisites

Before you begin, ensure you have:

- [Terraform](https://developer.hashicorp.com/terraform/downloads) installed (**v1.5+ recommended**)
- An AWS account with IAM permissions to create EC2, VPC, and Security Groups
- AWS credentials configured locally:

```bash
aws configure
```

---

## 🚀 Deployment Steps

### 📥 Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/aws-ec2-terraform-deploy.git
cd aws-ec2-terraform-deploy
```

### ⚙️ Initialize Terraform
```bash
terraform init
```

### ✅ Validate configuration
```bash
terraform validate
```

### 📦 Deploy infrastructure
```bash
terraform apply --auto-approve
```

### 🌐 Access NGINX
After deployment, open the EC2 Public IP in your browser to view the NGINX welcome page.

---

## 🧹 Cleanup
To avoid AWS charges, destroy the infrastructure when done:
```bash
terraform destroy --auto-approve
```
