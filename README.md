# 🚀 JobLink – Job & Study Resource Platform

JobLink is a full-stack web application built with Django that helps students and fresh graduates discover job opportunities and access high-quality study resources — all in one place.

---

## 🌐 Live Demo

👉 https://joblink-727200458275.asia-south1.run.app

---

## 📌 Features

* 🔍 Browse latest job listings (government, private, internships)
* 📚 Access free study resources (PDFs, notes, previous papers)
* 🧾 Clean and responsive UI (Tailwind CSS)
* 🧑‍💻 Admin panel for managing jobs and resources
* 📬 Contact form for user queries
* ⚡ Fast and scalable deployment using Docker + Cloud Run

---

## 🏗️ Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML, Tailwind CSS
* JavaScript

### Database

* SQLite (current)
* PostgreSQL (planned via Cloud SQL)

### DevOps & Deployment

* Docker
* Google Cloud Run
* GitHub Actions (CI/CD)

---

## 🧠 Architecture

```
User → Browser → Cloud Run (Django App)
                     ↓
                Database
```

---

## ⚙️ Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/joblink.git
cd joblink
```

---

### 2. Run with Docker

```bash
docker-compose up --build
```

---

### 3. Apply migrations

```bash
docker-compose exec web python manage.py migrate
```

---

### 4. Create superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

---

### 5. Access the app

* App: http://localhost:8000
* Admin: http://localhost:8000/admin

---

## 🚀 Deployment

This project is deployed using:

* Docker containerization
* Google Cloud Run (serverless deployment)

Manual deploy:

```bash
gcloud run deploy joblink --source . --region asia-south1 --allow-unauthenticated
```

---

## 🔄 CI/CD Pipeline

Automated deployment is handled using GitHub Actions:

* Push to `main` branch triggers deployment
* Builds Docker image
* Deploys to Google Cloud Run

---

## ⚠️ Notes

* SQLite is currently used for quick deployment (not recommended for production)
* Future upgrade: migrate to Google Cloud SQL (PostgreSQL)
* Static files are served using WhiteNoise

---

## 🛠️ Future Improvements

* 🔐 Authentication system (login/register)
* 🔎 Advanced job search & filtering
* 📊 User dashboard
* ☁️ PostgreSQL integration via Cloud SQL
* 🌍 Custom domain setup
* 📈 SEO optimization

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📧 Contact

For queries or collaboration:

* Email: [your-email@example.com](mailto:your-email@example.com)

---

## 📄 License

This project is open-source and available under the MIT License.

---

## ⭐ Acknowledgements

* Django documentation
* Tailwind CSS
* Google Cloud Platform

---

> Built with ❤️ by Rohit
