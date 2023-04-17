from utils import utils
import os


def main():
    path_to_operations = os.path.join("data", "operations.json")
    transaction_information = utils.load_data(path_to_operations)
    filt_data = utils.filt_state(transaction_information)
    sort_data = utils.data_sorting(filt_data)
    get_data = utils.get_formatted_data(sort_data)
    print(get_data)
    return get_data


if __name__ == "__main__":
    main()
