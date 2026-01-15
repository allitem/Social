from fastapi import FastAPI
from core.registry.module_registry import load_modules

app = FastAPI()
modules = load_modules()

@app.get("/modules")
def list_modules():
    return modules

@app.get("/health")
def health():
    return {"status": "ok"}
