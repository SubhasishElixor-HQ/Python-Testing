# Phase 11 — Performance and load testing

Locust scenario targets a local demo FastAPI app. Start the demo app first and use a small number of users. Never load-test production or third-party systems without authorization.

Run the demo API in a terminal:
```powershell
uv run uvicorn practice.api_app:app --host 127.0.0.1 --port 8000
```
In another terminal:
```powershell
uv run locust -f phases/phase_11_performance_load/locustfile.py --host http://127.0.0.1:8000
```
Open `http://localhost:8089` and start with a small number of users.
