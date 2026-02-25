# 🚦 Smart Traffic Platform

AI-powered smart traffic management platform featuring real-time vehicle detection, adaptive signal control, and an admin dashboard.

## Architecture

```
smart-traffic-platform/
├── apps/
│   ├── api/               # Node.js + Express backend
│   └── web/               # Next.js admin dashboard
├── packages/
│   └── ml-services/       # Python ML service (YOLOv8 + OpenCV)
└── supabase/              # Supabase configuration & migrations
```

## Sub-Projects

| Project | Stack | Description |
|---------|-------|-------------|
| **ML Service** | Python · YOLOv8 · OpenCV · FastAPI | Real-time vehicle detection & traffic analysis |
| **Backend** | Node.js · Express · Supabase | REST API, business logic, and data persistence |
| **Frontend** | Next.js · TypeScript · Tailwind CSS | Admin dashboard for monitoring & configuration |

## Quick Start

### Prerequisites
- Node.js ≥ 18
- Python ≥ 3.10
- npm ≥ 9

### 1. Install Node Dependencies
```bash
npm install
```

### 2. ML Service
```bash
cd packages/ml-services
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 3. Backend
```bash
npm run dev:api
```

### 4. Frontend
```bash
npm run dev:web
```

## License
MIT