# ☸️ Scalable Microservices Deployment on Kubernetes

## 📌 Project Overview
Designed and deployed a highly available Python web application using **Docker** and **Kubernetes**. 
The architecture features a self-healing deployment with 3 replicas and a Load Balancer for traffic distribution.

## 🛠 Tech Stack
- **Containerization:** Docker (Multi-stage build)
- **Orchestration:** Kubernetes (Deployment, Service, ReplicaSets)
- **Language:** Python (Flask)
- **Infrastructure:** Minikube / Local K8s Cluster

## 📸 Architecture & Proof
### 1. High Availability Status
(!1)[/images/kube.png]

### 2. Load Balancing in Action
*(Paste your browser screenshot showing different Pod IDs here)*
(!2)[/images/1.png]
(!3)[/images/2-.png]
(!4)[/images/3-.png]
## 🚀 How to Run
1. Build the image: `docker build -t my-k8s-app:v1 .`
2. Apply Manifests: `kubectl apply -f k8s/`
3. Access Service: `localhost:80`
