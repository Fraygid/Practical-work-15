print('Символы, которые можно использовать для лабиринта: ')
print('0 — проход (можно идти)')
print('1 — стена (нельзя пройти)')
print('л — ловушка (-10 HP)')
print('м — монета (+1 монета)')
print('ф — выход (нужно дойти до него и не погибнуть)')
print('з — враг (-50 HP)')
print('н — начальная точка (вход)')

labirint_input = input('Введите строку лабиринта(25 символов): ')

if len(labirint_input) != 25:
    print(f'Ошибка: нужно 25 символов, получено {len(labirint_input)}')
else:
    # Задание 1.1

    lab_rows = []

    print('Вид лабиринта: ')

    for i in range(0,25,5):
        row = labirint_input[i:i+5]
        lab_rows.append(row)
        print(row)

    # Задание 1.2

    enterance_row, enterance_col = -1, -1

    for i in range(5):
        for j in range(5):
            if lab_rows[i][j] == 'н':
                enterance_row, enterance_col = i, j
                break
        if enterance_row != -1:
            break

    if enterance_col != -1:
        print(f'Вход находится в строке {enterance_row}, столбце {enterance_col}')
    else:
        print('Вход не найден')

    # Задание 1.3

    exit_row, exit_col = -1, -1

    for i in range(5):
        for j in range(5):
            if lab_rows[i][j] == 'ф':
                exit_row, exit_col = i, j
                break
        if exit_row != -1:
            break

    if exit_col != -1:
        print(f'Выход находится в строке {exit_row}, столбце {exit_col}')
    else:
        print('Выход не найден')

    # Задание 1.4

    if enterance_row != -1 and exit_row != -1:
        distance = abs(enterance_row - exit_row) + abs(enterance_col - exit_col)
        print(f'Манхэттенсоке расстояние: {distance} шагов')
    else:
        print('Не удалось вычислить расстояние')

    # Задание 1.5

    coin_count = labirint_input.count('м')

    if coin_count > 0:
        coins_emoji = '🟡' * coin_count
        print(f'Монеты: {coins_emoji} * {coin_count}')
    else:
        print('Монет в лабиринте нет')

    # Задание 1.6

    traps_count = labirint_input.count('л')
    enemies_count = labirint_input.count('з')

    damage = traps_count * 10 + enemies_count * 50
    initial_hp = 100
    remaining_hp = max(0, initial_hp - damage)

    full_hearts = remaining_hp // 10
    empty_hearts = (initial_hp - remaining_hp) // 10

    health_bar = '♥' * full_hearts + '♡' * empty_hearts

    print(f'Ловушек: {traps_count} * (-10 HP) = -{traps_count * 10} HP')
    print(f'Врагов: {enemies_count} * (-50 HP) = -{enemies_count * 50} HP')
    print(f'Общий урон: {damage} HP')
    print(f'Оставшееся здоровье: {remaining_hp} HP')
    print(f'Визуализация: {health_bar}')

    # Задание 1.7

    emoji_dict = {
        '0': '⬜',
        '1': '⬛',
        'л': '🔷',
        'м': '🟡',
        'ф': '🏾',
        'з': '🐷',
        'н': '⭐'
    }

    emoji_lab_rows = []

    for row in lab_rows:
        emoji_row = ''.join(emoji_dict.get(char, '') for char in row)
        emoji_lab_rows.append(emoji_row)
        print(emoji_row)
