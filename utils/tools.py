import json


def load_json_dump(text, default_value=None):
    try:
        data = json.loads(text)
    except Exception as e:
        return default_value
    return data