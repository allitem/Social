import yaml, os

def load_modules(path="modules"):
    modules = {}
    for name in os.listdir(path):
        meta = os.path.join(path, name, "module.yaml")
        if os.path.isfile(meta):
            with open(meta) as f:
                modules[name] = yaml.safe_load(f)
    return modules
