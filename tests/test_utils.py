from utils import utils
import json
import os
from datetime import datetime
import pytest


def test_load_data():
    """Проверяем путь до файла и вывод содержимого файла"""
    path = os.path.join("tests", "test_operations.json")
    if not os.path.exists(path):
        assert utils.load_data(path) == []
    assert utils.load_data(path) == "letter"


def test_filt_state(test_data):
    """Проверяем фильтрацию полученных данных (выводим данные со статусом 'EXECUTED'"""
    assert utils.filt_state(test_data) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        }
    ]


def test_data_sorting(test_data):
    """Проверяем сортировку полученных данных по дате (от новых к старым)"""
    assert utils.data_sorting(test_data) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },
    ]


def test_get_formatted_data(test_data):
    """Проверяем вывод полученных данных по форме"""
    formatted_data = utils.get_formatted_data(test_data)
    assert formatted_data == \
("""26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб.

12.09.2018 Перевод организации
Visa Platinum 1246 37** **** 3588 -> Счет **1657
67314.70 руб.

13.07.2019 Открытие вклада
Счет **2265
97853.86 руб.
""")
    assert [data_dict['date'] for data_dict in test_data] == ["2019-08-26T10:50:58.294041",
                                                              "2018-09-12T21:27:25.241689",
                                                              "2019-07-13T18:51:29.313309"]
    date_list = []
    for data_dict in test_data:
        date_list.append(datetime.strptime(data_dict['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y"))
    assert date_list == ['26.08.2019', '12.09.2018', '13.07.2019']

