import json
import os


def load_data(path):
    """Загружает данные по операциям из файла"""
    if not os.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        operations = json.load(file)
    return operations


