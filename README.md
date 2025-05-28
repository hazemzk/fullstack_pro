# 📦 Inventory Management System

A modern, full-stack Inventory Management Application built with **FastAPI** for the backend and **React** for the frontend. This project is part of a hands-on series focused on combining Python and JavaScript technologies to build real-world business applications.

## 🚀 Tech Stack

- ⚙️ **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- 💻 **Frontend**: [React.js](https://reactjs.org/)
- 💾 **Database**: SQLite or PostgreSQL (can be easily switched)
- 📬 **Email Support**: Built-in email functionality using FastAPI's background tasks
- 🎨 **UI Framework**: Bootstrap (via React-Bootstrap)

---

## ✨ Features

- ✅ Full CRUD (Create, Read, Update, Delete) for product inventory
- 🔍 Product search functionality
- 📧 Send emails (e.g., on updates or alerts)
- 📊 Live stock and sales tracking (quantity in stock, quantity sold, revenue)
- 🧼 Clean and intuitive UI with Bootstrap
- ⚡ Fast and lightweight API with automatic Swagger docs

---

## 📁 Project Structure
/backend
└── main.py (FastAPI server)
└── models.py
└── routes/
└── database.py
/frontend
└── src/
├── components/
├── ProductContext.js
├── App.js
└── ...
## 🛠️ Setup Instructions

### 1. Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### 2.Frontend

cd frontend
npm install
npm start

📬 Email Functionality
To enable email notifications:

Configure your SMTP settings in the FastAPI backend (e.g., Gmail SMTP or Mailgun).

Use background tasks to send emails without blocking API responses.
