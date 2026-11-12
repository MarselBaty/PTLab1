
# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from CalcAcademicDebt import CalcAcademicDebt
from TextDataReader import TextDataReader
from JSONDataReader import JSONDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if path.endswith(".json"):
        reader = JSONDataReader()
    else:
        reader = TextDataReader()

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    academic_debts = CalcAcademicDebt(students).calc()
    print("Students with academic debts: ", academic_debts)


if __name__ == "__main__":
    main()
