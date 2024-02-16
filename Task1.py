#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    school = {
        '1а': 17,
        '1б': 30,
        '2б': 28,
        '6а': 19,
        '7в': 15,
    }

    print("Исходный словарь:")
    print(school)

    total_students = sum(school.values())
    print("\nОбщее количество учащихся в школе:", total_students)
    # Задача а)
    school['1а'] = 21
    # Задача б)
    school['8г'] = 26
    # Задача с)
    if '2б' in school:
        del school['2б']

    print("\nИзмененный словарь:")
    print(school)

    total_students = sum(school.values())
    print("\nОбщее количество учащихся в школе:", total_students)
