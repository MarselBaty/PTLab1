
# -*- coding: utf-8 -*-

from Types import DataType


class CalcAcademicDebt:

    def __init__(self, students: DataType) -> None:
        self.students = students

    def calc(self) -> int:
        count = 0

        for subjects in self.students.values():
            if any(score < 61 for _, score in subjects):
                count += 1

        return count
