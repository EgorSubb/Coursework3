import json
import os
from datetime import datetime
# from operator import attrgetter


def load_data(path):
    """Загружает данные по операциям из файла"""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        operations = json.load(file)
    return operations


def filt_state(data):
    """Фильтрует загруженные из файла данные по статусу ('EXECUTED')"""
    filt_data = [data_dict for data_dict in data if 'state' in data_dict and data_dict['state'] == 'EXECUTED']
    return filt_data


def data_sorting(filter_data):
    """Фильтрует загруженные из файла данные по дате и выдает последние 5 операций (от новых к старым)"""
    data = sorted(filter_data, key=lambda date: date['date'])
    last_operations = data[-5:]
    sort_by_date = last_operations[::-1]
    return sort_by_date
    # data = sorted(filter_data, key=attrgetter('date'))
    # sort_by_date = data[::-1]
    # return sort_by_date


def get_formatted_data(sort_data):
    """Преобразует отсортированнные данные в читаемый вид"""
    formatted_data = []
    for data_dict in sort_data:
        date = datetime.strptime(data_dict['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = data_dict['description']
        if 'from' in data_dict:
            sender = data_dict['from'].split()
            sender_name = " ".join(sender[:-1])
            sender_number = sender[-1]
            sender_secret_number = f" {sender_number[:4]} {sender_number[4:6]}** **** {sender_number[-4:]} "
            arrow = "-> "
        else:
            sender_name = ''
            sender_secret_number = ''
            arrow = ''
        recipient = data_dict['to'].split()
        recipient_name = " ".join(recipient[:-1])
        recipient_number = recipient[-1]
        recipient_secret_number = f"**{recipient_number[-4:]}"
        payment = data_dict['operationAmount']['amount']
        currency = data_dict['operationAmount']['currency']['name']
        formatted_data.append(
            f"{date} {description}\n{sender_name}{sender_secret_number}{arrow}{recipient_name} {recipient_secret_number}\n{payment} {currency}\n")
    return "\n".join(formatted_data)
