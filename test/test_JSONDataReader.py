
# -*- coding: utf-8 -*-
import json

from src.JSONDataReader import JSONDataReader


def test_read_json(tmp_path):
    data = {
        "Иванов Иван Иванович": {
            "математика": 80,
            "программирование": 90
        },
        "Петров Петр Петрович": {
            "химия": 50
        }
    }

    file_path = tmp_path / "data.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)

    reader = JSONDataReader()
    students = reader.read(str(file_path))

    assert students == {
        "Иванов Иван Иванович": [
            ("математика", 80),
            ("программирование", 90)
        ],
        "Петров Петр Петрович": [
            ("химия", 50)
        ]
    }
