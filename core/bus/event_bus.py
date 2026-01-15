_subscribers = {}

def publish(event: str, payload: dict):
    for cb in _subscribers.get(event, []):
        cb(payload)

def subscribe(event: str, callback):
    _subscribers.setdefault(event, []).append(callback)
# core/registry/module_registry.py
from core.bus.event_bus import subscribe

def register_module(name, events):
    for ev in events.get("subscribe", []):
        subscribe(ev, lambda payload: print(f"{name} received {ev}"))
