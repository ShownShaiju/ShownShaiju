# Hi, I'm Shown Shaiju 👋

**Cloud & DevOps Engineer** · AWS Certified Solutions Architect – Associate (SAA-C03)  
Building real systems, documenting real failures, learning in public.

[![AWS SAA-C03](https://img.shields.io/badge/AWS_SAA--C03-Certified-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white)](https://www.credly.com/badges/9e2850a5-6b19-4017-9df5-8858c49b517d)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-shownshaiju-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/shownshaiju)
[![Location](https://img.shields.io/badge/Kerala,_India-Cloud_Engineer-232F3E?style=for-the-badge&logo=googlemaps&logoColor=white)](https://github.com/ShownShaiju)

---

## 🚀 What I've Built

### DevRPG — 5-Tier Cloud-Native Platform
> Django · Celery · Redis · PostgreSQL · Nginx · Docker · Kubernetes · AWS EKS · S3

Containerized and deployed a full 5-tier decoupled monolith to Amazon EKS. Not a tutorial follow-along — a real deployment with real failures.

**What I actually debugged:**
- 🔧 Refactored Celery image pipeline to run entirely in-memory via `io.BytesIO` — S3 objects have no local paths
- 🔧 Diagnosed a Docker phantom bind-mount bug (directory created where a file should be)
- 🔧 Traced a cascading `SyntaxError` that flatlined the entire compute layer via shared Docker image
- 🔧 Identified and fixed an Nginx DNS cache trap — stale IP after container rebuild caused 502s
- 🔧 Resolved Kubernetes `CrashLoopBackOff` from missing EBS CSI driver and OIDC trust misconfiguration
- 🔧 Fixed a Postgres `initdb` failure caused by AWS formatting a `lost+found` dir on fresh EBS volume
- 🔧 Caught a trailing whitespace POSIX violation in a `kubectl` secret

👉 [View Repository](https://github.com/ShownShaiju/DevRPG)

---

### AWS Learning Notes
> 13 days of structured study → SAA-C03 passed first attempt

Day-by-day documented learning — architecture patterns, failure modes, cost behavior.

👉 [View Notes](https://github.com/ShownShaiju/aws-learning)

---

## 🛠️ Tech Stack

**Cloud & Infra**  
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?style=flat&logo=amazonaws&logoColor=white)
![Amazon EKS](https://img.shields.io/badge/Amazon_EKS-Kubernetes-orange?style=flat&logo=amazonaws)
![S3](https://img.shields.io/badge/S3-Storage-green?style=flat&logo=amazonaws)
![VPC](https://img.shields.io/badge/VPC-Networking-blue?style=flat&logo=amazonaws)
![IAM](https://img.shields.io/badge/IAM-Security-red?style=flat&logo=amazonaws)

**Containers & Orchestration**  
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=flat&logo=kubernetes&logoColor=white)

**Backend & Tools**  
![Python](https://img.shields.io/badge/Python-Programming-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?style=flat&logo=django&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Reverse_Proxy-009639?style=flat&logo=nginx&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-Message_Broker-DC382D?style=flat&logo=redis&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=flat&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Advanced-FCC624?style=flat&logo=linux&logoColor=black)

---

## 📊 GitHub Stats

![Shown's GitHub Stats](https://github-readme-stats.vercel.app/api?username=ShownShaiju&show_icons=true&theme=tokyonight&hide_border=true&count_private=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=ShownShaiju&layout=compact&theme=tokyonight&hide_border=true)

![GitHub Streak](https://streak-stats.demolab.com?user=ShownShaiju&theme=tokyonight&hide_border=true)

---

## 🎯 Currently Learning

- Terraform (Infrastructure as Code)
- Cloud Resume Challenge — Lambda, API Gateway, DynamoDB, CloudFront
- Kubernetes internals — understanding what I've already deployed, from first principles

---

## 📍 Where I'm Headed

Cloud Security & DevOps. Specifically — building toward **AWS Security Specialty** after establishing solid infrastructure fundamentals. Long game.

---

*"Ship real things. Document real failures. The rest follows."*
