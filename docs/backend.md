# SecureVEA Fraud Check MVP

### Backend (FastAPI)
- Provides REST API endpoints for fraud-related checks such as SIM swap, device swap, call forwarding, and retrieval of related event dates, location retrieval and verification etc.
- Acts as a secure intermediary managing authentication, CORS, request validation, and orchestration across multiple APIs.
- Built with Python and FastAPI for asynchronous and high-performance web services.


## Backend Setup

### Prerequisites
- Python 3.12+
- Virtual environment support (`venv`)

### Installation & Running

Create and activate a virtual environment (Unix-based)

```
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

On Windows CMD shell:

```
cd backend
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies
```
pip install -r requirements.txt
```

Run backend server
```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Backend runs at `http://localhost:8000`.

Visit docs at `http://localhost:8000/docs`.