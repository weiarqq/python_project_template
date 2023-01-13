import os
import yaml
import sys

BASE_PATH = os.path.dirname(__file__)
# 读取当前环境
env = os.environ.get("ALGORITHM_ENV", 'test')
# 根据当前环境读取对应的配置文件
filepath = os.path.join(BASE_PATH, f'application-{env}.yml')
with open(filepath, "r") as f:
    yaml_config = yaml.safe_load(f)
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
BASE_PATH = os.path.dirname(__file__)
sys.path.append(PROJECT_PATH)


class Config:
    pass


def to_obj(obj: object, data):
    if not isinstance(data, dict):
        raise ValueError("data is not dict")
    for key in data:
        if isinstance(data[key], dict):
            key_obj = Config()
            to_obj(key_obj, data[key])
            setattr(obj, key, key_obj)
        else:
            setattr(obj, key, data[key])


config = Config()
to_obj(config, yaml_config)