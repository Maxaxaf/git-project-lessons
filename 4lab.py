# -*- coding: utf-8 -*-
# ВАРИАНТ 7 - Задания 1 и 2
# Универсум U = {0,1,2,3,4,5,6,7,8,9}
# Множества: A={1,2,3}, B={0,1,2,5,8}, C={0,2,5,8}, D={3,6,8,9}

# ============================================================
# ФУНКЦИИ
# ============================================================

def SET_convert_list_to_bin(M_list):
    M_bin = [0] * 10
    for elem in M_list:
        M_bin[elem] = 1
    return M_bin


def SET_convert_bin_to_list(M_bin):
    return [i for i in range(10) if M_bin[i]]


def SET_bin_union(A, B):
    return [1 if (a or b) else 0 for a, b in zip(A, B)]


def SET_bin_intersection(A, B):
    return [1 if (a and b) else 0 for a, b in zip(A, B)]


def SET_bin_difference(A, B):
    return [1 if (a and not b) else 0 for a, b in zip(A, B)]


def SET_bin_complement(A):
    return [1 if not a else 0 for a in A]


def cartesian_product(A, B):
    """Декартово произведение A x B"""
    return [(a, b) for a in A for b in B]


def power_set(S):
    """Булеан (множество всех подмножеств)"""
    res = [[]]
    for x in S:
        res += [sub + [x] for sub in res]
    return res


# ============================================================
# ВЫПОЛНЕНИЕ
# ============================================================

if __name__ == "__main__":
    # Исходные данные
    A = [1, 2, 3]
    B = [0, 1, 2, 5, 8]
    C = [0, 2, 5, 8]
    D = [3, 6, 8, 9]

    # --- ЗАДАНИЕ 1 ---
    # Вычислить: A ∩ C̅ ∪ (B ∪ D)

    A_bin = SET_convert_list_to_bin(A)
    B_bin = SET_convert_list_to_bin(B)
    C_bin = SET_convert_list_to_bin(C)
    D_bin = SET_convert_list_to_bin(D)

    # Шаги вычисления
    C_compl_bin = SET_bin_complement(C_bin)
    AC_compl_bin = SET_bin_intersection(A_bin, C_compl_bin)
    BD_union_bin = SET_bin_union(B_bin, D_bin)
    result_bin = SET_bin_union(AC_compl_bin, BD_union_bin)

    # Вывод
    print(SET_convert_bin_to_list(result_bin))

    # --- ЗАДАНИЕ 2 ---
    # 1. Декартово произведение A x B
    # 2. Булеан P(A)

    print(cartesian_product(A, B))
    print(power_set(A))