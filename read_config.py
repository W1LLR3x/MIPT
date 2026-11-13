import yaml

with open(".venv/config.yaml", 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)
print(data)