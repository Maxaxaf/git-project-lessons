# 1-2

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


#3

def pairs_to_matrix(pairs, domain, codomain):
    """Преобразует список пар в булеву матрицу"""
    m, n = len(domain), len(codomain)
    mat = [[0] * n for _ in range(m)]
    dom_idx = {x: i for i, x in enumerate(domain)}
    cod_idx = {y: j for j, y in enumerate(codomain)}
    for a, b in pairs:
        if a in dom_idx and b in cod_idx:
            mat[dom_idx[a]][cod_idx[b]] = 1
    return mat


def check_rel_properties_inter(mat):
    """Проверка свойств отношения между разными множествами"""
    m = len(mat)
    n = len(mat[0]) if mat else 0

    totality = all(any(row) for row in mat)
    functionality = all(sum(row) <= 1 for row in mat)
    surjectivity = all(any(mat[i][j] for i in range(m)) for j in range(n))
    injectivity = all(sum(mat[i][j] for i in range(m)) <= 1 for j in range(n))
    bijectivity = totality and functionality and surjectivity and injectivity

    return {
        "totality": totality,
        "functionality": functionality,
        "surjectivity": surjectivity,
        "injectivity": injectivity,
        "bijectivity": bijectivity
    }


def compose_relations(R, S):
    """Суперпозиция S  R (булево умножение матриц)"""
    m = len(R)
    k = len(S)
    n = len(S[0]) if S else 0
    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = int(any(R[i][l] and S[l][j] for l in range(k)))
    return res


# 4

def check_rel_properties_single(mat):
    """Проверка свойств отношения на одном множестве"""
    n = len(mat)
    reflexive = all(mat[i][i] == 1 for i in range(n))
    symmetric = all(mat[i][j] == mat[j][i] for i in range(n) for j in range(n))
    antisymmetric = all(not (mat[i][j] == 1 and mat[j][i] == 1) for i in range(n) for j in range(i + 1, n))
    transitive = all(
        not (mat[i][j] == 1 and mat[j][k] == 1) or mat[i][k] == 1 for i in range(n) for j in range(n) for k in range(n))

    return {
        "reflexive": reflexive,
        "symmetric": symmetric,
        "antisymmetric": antisymmetric,
        "transitive": transitive
    }


# 5

def find_equivalence_classes(mat, elements):
    """Перечисление классов эквивалентности (обход в глубину)"""
    n = len(mat)
    visited = [False] * n
    classes = []
    for i in range(n):
        if not visited[i]:
            current_class = []
            stack = [i]
            while stack:
                curr = stack.pop()
                if not visited[curr]:
                    visited[curr] = True
                    current_class.append(elements[curr])
                    for next_idx in range(n):
                        if mat[curr][next_idx] == 1 and not visited[next_idx]:
                            stack.append(next_idx)
            classes.append(sorted(current_class))
    return classes


if __name__ == "__main__":
    A = [1, 2, 3]
    B = [0, 1, 2, 5, 8]
    C = [0, 2, 5, 8]
    D = [3, 6, 8, 9]

    #1
    print("1")
    A_bin = SET_convert_list_to_bin(A)
    B_bin = SET_convert_list_to_bin(B)
    C_bin = SET_convert_list_to_bin(C)
    D_bin = SET_convert_list_to_bin(D)

    C_compl_bin = SET_bin_complement(C_bin)
    AC_compl_bin = SET_bin_intersection(A_bin, C_compl_bin)
    BD_union_bin = SET_bin_union(B_bin, D_bin)
    result_bin = SET_bin_union(AC_compl_bin, BD_union_bin)
    print(SET_convert_bin_to_list(result_bin))

    #2
    print("\n2")
    print(cartesian_product(A, B))
    print(power_set(A))

    #3
    print("\n3")
    R1_pairs = [(1, 0), (2, 2), (3, 8)]  # Отношение A → B
    R2_pairs = [(0, 0), (2, 5), (8, 8)]  # Отношение B → C
    R1_mat = pairs_to_matrix(R1_pairs, A, B)
    R2_mat = pairs_to_matrix(R2_pairs, B, C)

    print("Свойства R1:", check_rel_properties_inter(R1_mat))
    print("Свойства R2:", check_rel_properties_inter(R2_mat))

    comp_mat = compose_relations(R1_mat, R2_mat)
    comp_pairs = [(A[i], C[j]) for i in range(len(A)) for j in range(len(C)) if comp_mat[i][j]]
    print("Суперпозиция R2∘R1:", comp_pairs)

    #4
    print("\n4")
    Eq_pairs = [(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)]  # Отношение на A
    Eq_mat = pairs_to_matrix(Eq_pairs, A, A)
    print("Свойства отношения на A:", check_rel_properties_single(Eq_mat))

    #5
    print("\n5")
    print("Классы эквивалентности на A:", find_equivalence_classes(Eq_mat, A))