from fastapi import FastAPI

app = FastAPI(title="DroneDesk")


@app.get("/health")
def health():
    return {"status": "ok"}
