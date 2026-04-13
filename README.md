# 🚀 2-Tier Docker Application (Flask + MySQL)

## 📌 Project Overview

This project is a **2-tier containerized application** built using:

- **Flask (Python)** → Backend API
- **MySQL** → Database
- **Docker & Docker Compose** → Containerization and orchestration

The application provides **CRUD APIs** with secure authentication and persistent database storage.

---

## 🧱 Architecture
User → Flask App (API) → MySQL Database
│
Docker Container
│
Docker Compose Network


---

## ⚙️ Tech Stack

- Python (Flask)
- MySQL 8.0
- Docker
- Docker Compose
- JWT Authentication
- Password Hashing

---

## 📁 Project Structure


.
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── backup.sql
├── .env.example
├── .gitignore


---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd docker-app-v2
2. Create Environment File
cp .env.example .env

Edit .env with your values.

3. Run Application
docker-compose up --build
4. Access Application
http://localhost:5000

🔐 Authentication
User-based login system
JWT token authentication
Password hashing implemented for security
🧪 API Features
Create data
Read data
Update data
Delete data
Secure endpoints using JWT

💾 Database Persistence
MySQL data is stored using Docker volumes
Data remains safe even after container restart

📦 Backup & Restore
Backup
docker exec <mysql-container> mysqldump -u root -p <db_name> > backup.sql
Restore
docker exec -i <mysql-container> mysql -u root -p <db_name> < backup.sql

🐳 Docker Hub (Optional)
Push Image
docker tag <image> <dockerhub-username>/<repo>:tag
docker push <dockerhub-username>/<repo>:tag
Pull Image
docker pull <dockerhub-username>/<repo>:tag

⚠️ Troubleshooting
App not starting
Check logs:
docker-compose logs
DB connection issue
Ensure correct .env values
Check container status:
docker ps
Port already in use
Change port in docker-compose.yml

🎯 Key Features
2-tier architecture
Containerized deployment
Secure authentication (JWT)
Persistent storage
Backup & restore support
Production-ready structure

🚀 Future Improvements
Prometheus & Grafana monitoring
CI/CD pipeline (Jenkins/GitHub Actions)
Kubernetes deployment
Load balancing & auto-scaling

👨‍💻 Author

Abhishek Makwana

📜 License

This project is for learning and demonstration purposes.
