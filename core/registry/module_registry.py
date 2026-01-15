import yaml, os

def load_modules(path="modules"):
    modules = {}
    for name in os.listdir(path):
        meta = os.path.join(path, name, "module.yaml")
        if os.path.isfile(meta):
            with open(meta) as f:
                modules[name] = yaml.safe_load(f)
    return modules
# core/registry/module_registry.py
from core.bus.event_bus import subscribe

def register_module(name, events):
    for ev in events.get("subscribe", []):
        subscribe(ev, lambda payload: print(f"{name} received {ev}"))
