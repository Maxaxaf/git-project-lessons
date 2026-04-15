def check_t0(tt):
    return tt[0] == 0


def check_t1(tt):
    return tt[-1] == 1


def check_s(tt):
    # Самодвойственность: f(00)!=f(11) и f(01)!=f(10)
    return tt[0] != tt[3] and tt[1] != tt[2]


def check_l(tt):
    # Линейные функции для 2 переменных (всего 8 штук)
    linear = [
        [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 1, 1], [0, 1, 0, 1],
        [1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]
    ]
    return tt in linear


def check_m(tt):
    # Монотонность: сравнение по всем парам, где x <= y
    return tt[0] <= tt[1] and tt[0] <= tt[2] and \
        tt[1] <= tt[3] and tt[2] <= tt[3]


# 1. Проверка полноты по готовой таблице Поста (матрица 0/1)
def is_complete(post_table):
    classes = ["T0", "T1", "S", "L", "M"]
    for j, name in enumerate(classes):
        col = [row[j] for row in post_table]
        if all(col):  # Если весь столбец заполнен единицами
            print(f"СИСТЕМА НЕ ПОЛНАЯ. Все функции лежат в классе {name}.")
            return False
    print("СИСТЕМА ПОЛНАЯ. В каждом классе есть нарушитель.")
    return True


# 2. Заполнение таблицы Поста и вывод
def build_post_table(functions):
    checks = [check_t0, check_t1, check_s, check_l, check_m]
    names = ["T0", "T1", "S", "L", "M"]
    table = []

    print("\nТаблица Поста (1 - принадлежит, 0 - нет):")
    print("Функция | T0 | T1 | S  | L  | M")

    for i, tt in enumerate(functions):
        row = []
        print(f"  {i + 1}    |", end="")
        for check in checks:
            val = 1 if check(tt) else 0
            row.append(val)
            print(f" {val}  |", end="")
        print()
        table.append(row)

    print()
    # 1. Сразу определяем полноту по полученной таблице
    is_complete(table)
    return table


# 3. Ввод и построение таблицы истинности
def main():
    try:
        n = int(input("Количество функций в системе: "))
    except ValueError:
        print("Ошибка ввода. Нужно число.")
        return

    funcs = []
    for i in range(n):
        print(f"\n--- Функция {i + 1} ---")
        vals = input("Введите 4 значения f(00) f(01) f(10) f(11) через пробел: ").split()
        tt = [int(v) for v in vals]

        if len(tt) != 4 or any(v not in (0, 1) for v in tt):
            print("Неверный формат. Нужно ровно 4 нуля или единицы.")
            return

        print("\nТаблица истинности:")
        print(" x y | f")
        for j, v in enumerate(tt):
            print(f" {j >> 1} {j & 1} | {v}")

        funcs.append(tt)

    build_post_table(funcs)


if __name__ == "__main__":
    main()