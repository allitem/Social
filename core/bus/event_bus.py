_subscribers = {}

def publish(event: str, payload: dict):
    for cb in _subscribers.get(event, []):
        cb(payload)

def subscribe(event: str, callback):
    _subscribers.setdefault(event, []).append(callback)
