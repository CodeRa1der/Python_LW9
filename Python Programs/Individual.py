#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Список маршрутов
    routes = []
    number = 0
    # Начало бесконечного цикла команд
    while True:
        # Сюда вписывать команды
        command = input('>>> ').lower()

        # Команда help
        if command == 'help':
            print('\nСписок команд:')
            print('help - Вывести этот список')
            print('add - Добавить маршрут')
            print('list - Показать список маршрутов')
            print('exit - Выйти из программы')
        # Команда add
        elif command == 'add':
            # Запись данных маршрута
            first = input('Первая точка маршрута: ')
            second = input('Вторая точка маршрута: ')
            number += 1
            # Создание словаря
            route = {
                'first_checkpoint': first,
                'second_checkpoint': second,
                'number': number
            }

            # Добавление словаря в список
            routes.append(route)
            # Сортировка по номеру маршрута
            routes.sort(key=lambda item: item.get('number', ''))

        # Команда list
        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 14,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^5} | {:^20} | {:^20} |'.format(
                    "Номер маршрута",
                    "Место отправки",
                    "Место прибытия"
                )
            )
            print(line)
            # Вывод данных о маршрутах
            for route in routes:
                print(
                    '| {:<14} | {:<20} | {:<20} |'.format(
                        route.get('number', ''),
                        route.get('first_checkpoint', ''),
                        route.get('second_checkpoint', '')
                    )
                )
            print(line)

        # Команда exit
        elif command == 'exit':
            break
        # Другая команда/неверно введенная команда
        else:
            print(f'Неизвестная команда {command}')
