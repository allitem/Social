class StephenController:
    def allow(self, module_meta, action: str) -> bool:
        return module_meta.get("permissions", {}).get(action, False)

controller = StephenController()
