# TaxSync — GST Reconciliation MVP

**Reconcile Smarter. Manage Better.**

This is the initial runnable foundation for the first release: company setup, GSTIN association, GSTR-2B and purchase-register imports, invoice matching, mismatch review and reconciliation history.

## Stack
- React + Vite frontend
- Python FastAPI backend
- SQLAlchemy 2.x
- SQLite by default; PostgreSQL via `DATABASE_URL`
- CSV/XLSX/JSON/ZIP import
- Exact matching plus conservative fuzzy suggestions

## Requirements
Python 3.11+, Node.js 20+, npm.

## Windows setup

Backend (PowerShell):
```powershell
cd TaxSync\backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Frontend (second terminal):
```powershell
cd TaxSync\frontend
npm install
npm run dev
```
Open the Vite URL, normally http://localhost:5173. API docs: http://127.0.0.1:8000/docs.

## Linux/macOS
```bash
cd TaxSync/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```
In a second terminal:
```bash
cd TaxSync/frontend
npm install
npm run dev
```

## Database
Default SQLite: `sqlite:///./taxsync.db`. PostgreSQL example:
`postgresql+psycopg://taxsync:change-this-password@localhost:5432/taxsync`.

For LAN use, all clients must connect to a central FastAPI server. Do not share a SQLite database file over a network.

## Import columns
The import parser recognizes common aliases for supplier GSTIN, invoice number/date, taxable value, IGST, CGST, SGST, cess and invoice value. ZIP imports currently select the first supported CSV/JSON/XLSX file.

Import source values: `gstr2b` and `purchase_register`.

## API
- GET `/api/health`
- GET/POST `/api/companies`
- POST `/api/companies/{id}/imports?source=gstr2b`
- POST `/api/companies/{id}/reconcile`
- GET `/api/companies/{id}/reconciliations`
- GET `/api/reconciliations/{run_id}/results`

## Tests
```bash
cd backend
pytest
```

## Important limitations
This is a development scaffold, not production-ready tax software. Authentication/RBAC, production encryption and key management, Alembic migrations, decimal money precision, complete GST portal schema adapters, official integrations, PDF/Excel reporting, backup/recovery, installers and full security testing remain to be implemented. Do not use it to file returns or make tax decisions without professional review.
