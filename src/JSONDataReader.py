
# -*- coding: utf-8 -*-
import json

from Types import DataType
from DataReader import DataReader


class JSONDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = json.load(file)

        self.students = {}

        for student, subjects in data.items():
            self.students[student] = [
                (subject, int(score))
                for subject, score in subjects.items()
            ]

        return self.students
