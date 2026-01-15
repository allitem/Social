from core.bus.event_bus import publish

def run(payload: dict):
    result = {
        "summary": "scan complete",
        "score": 0.85
    }
    publish("content.scan.result", result)
    return result
