import os

import yaml


def base_dir():
    return os.path.dirname(os.path.abspath(__file__))


def read_config(section, key):
    file = base_dir() + '/config.yaml'
    with open(file, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data[section][key]