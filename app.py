
"""
TaxSync - GST Reconciliation Manager
Root application entry point for FastAPI.

Run locally:
    uvicorn app:app --reload

Deploy:
    uvicorn app:app --host 0.0.0.0 --port 8000
"""

from backend.app.main import app

# Export FastAPI application for Uvicorn and deployment platforms.
__all__ = ["app"]
