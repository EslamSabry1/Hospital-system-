# Hospital System (DeviceCare) 🏥

A comprehensive Django-based medical device inventory and maintenance management system. Built for hospitals to track devices, schedule maintenance, predict failures, and generate QR codes for equipment identification.

## ✨ Features

- 📱 **Device Inventory Tracking** - Complete device management with serialization
- 🔧 **Maintenance Scheduling** - Track preventive and corrective maintenance
- 🤖 **Failure Prediction** - AI-powered device failure forecasting
- 🔲 **QR Code Generation** - Auto-generate QR codes for device identification
- 📊 **Excel Export** - Export device data to Excel format
- 🌍 **Multi-Language Support** - English and Arabic localization
- 👥 **Department Management** - Organize devices by department
- 📈 **Analytics Dashboard** - Monitor device status and maintenance metrics
- 🐳 **Docker Ready** - Easy containerized deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (optional)
- Git

### Option 1: Docker (Recommended)

```bash
docker compose up --build
```

### Option 2: Local Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python reset_db.py
python manage.py runserver
```

Open http://127.0.0.1:8000

## 📦 Core Models

- **Device**: Medical equipment with tracking and QR codes
- **Department**: Hospital departments
- **Maintenance**: Maintenance records and history

## 🧪 Testing

```bash
python manage.py test devices
```

## 🔐 Security

- CSRF protection, SQL injection prevention
- User authentication required
- HTTPS ready configuration

## 🚀 Deployment

Supports Docker, Gunicorn, and traditional WSGI servers.

## 📖 API Endpoints

- `GET /devices/` - List all devices
- `POST /devices/create/` - Create new device
- `GET /devices/<id>/` - Device details
- `GET /export/excel/` - Export to Excel

## 👨‍💻 Author

**EslamSabry1** - GitHub: [@EslamSabry1](https://github.com/EslamSabry1)