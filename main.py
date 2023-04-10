from utils import utils
import os

path_to_operations = os.path.join("data", "operations.json")

print(utils.load_data(path_to_operations))