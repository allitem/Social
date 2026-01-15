from fastapi import FastAPI
from core.registry.module_registry import load_modules
from core.bus.event_bus import publish

app = FastAPI()
modules = load_modules()

@app.get("/modules")
def list_modules():
    return modules

@app.post("/invoke/{module}/{action}")
def invoke_module(module: str, action: str):
    publish(f"{module}.{action}", {})
    return {"status": "invoked", "module": module, "action": action}
