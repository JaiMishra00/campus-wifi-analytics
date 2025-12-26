from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import WifiScan
from app.store import save_scan, get_all_scans


app = FastAPI(title="WiFi Analytics Backend")

# allow browser access (important for phone)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "backend running"}

@app.post("/api/scan")
def ingest_scan(scan: WifiScan):
    save_scan(scan.dict())
    return {"message": "scan received"}

@app.get("/api/scans")
def read_scans():
    return get_all_scans()

@app.get("/api/heatmap")
def heatmap():
    return {
        "points": [
            {"x": 120, "y": 200, "value": 0.8},
            {"x": 300, "y": 100, "value": 0.4}
        ]
    }

