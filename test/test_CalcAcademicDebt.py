
# -*- coding: utf-8 -*-

from src.CalcAcademicDebt import CalcAcademicDebt


def test_no_academic_debts():
    students = {
        "Иванов": [("математика", 80), ("физика", 61)],
        "Петров": [("химия", 90), ("история", 75)]
    }

    assert CalcAcademicDebt(students).calc() == 0


def test_one_student_with_academic_debt():
    students = {
        "Иванов": [("математика", 50), ("физика", 80)],
        "Петров": [("химия", 90), ("история", 75)]
    }

    assert CalcAcademicDebt(students).calc() == 1


def test_multiple_students_with_academic_debts():
    students = {
        "Иванов": [("математика", 50), ("физика", 40)],
        "Петров": [("химия", 90), ("история", 60)],
        "Сидоров": [("математика", 30), ("физика", 80)]
    }

    assert CalcAcademicDebt(students).calc() == 3


def test_score_equal_to_61_is_not_academic_debt():
    students = {
        "Иванов": [("математика", 61)],
        "Петров": [("химия", 60)]
    }

    assert CalcAcademicDebt(students).calc() == 1


def test_empty_students():
    assert CalcAcademicDebt({}).calc() == 0
