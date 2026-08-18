from fastapi import FastAPI

app = FastAPI(
    title="NetPulse API",
    description="Wireless Network Monitoring Platform",
    version="1.0.0",
)


@app.get("/")
def main_page():
    return {"status": "ok", "main": "Welcome to Front page"}


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "netpulse-api"}
