# возвращает таблицу истинности по кортежу значений функции 3 переменных
def truth_table_by_vec(v):
    assert(len(v) == 8)
    tt = {}
    i = 0
    for A in range(2):
        for B in range(2):
            for C in range(2):
                tt[A, B, C] = v[i]
                i += 1
    return tt

v_var7 = (1, 1, 0, 1, 0, 0, 1, 1)
tt = truth_table_by_vec(v_var7)

# возвращает таблицу истинности по заданной функции 3 переменных
def truth_table_by_func(f):
    tt = {}
    for A in range(2):
        for B in range(2):
            for C in range(2):
                tt[A, B, C] = int(f(A, B, C))
    return tt

def f_maj(x, y, z):
    return x and y or x and z or y and z

v_var7 = (1, 1, 0, 1, 0, 0, 1, 1)
tt = truth_table_by_vec(v_var7)

#tt = truth_table_by_func(f_maj)
# tt = truth_table_by_func(f)
print(tt)

# принимает на вход таблицу истинности и выдает строку с СДНФ
def fdnf(tt):
   return ' | '.join(map(conj_str, [key for key in tt if tt[key]]))

# принимает на вход кортеж значений переменных и выдает элементарную конъюнкцию с такими степенями переменных
def conj_str(vars):
    var_names = ('x', 'y', 'z')
    return '&'.join(map(literal_str, var_names, vars))

# принимает на вход имя переменной (str) и ее степень (bool), возвращает литерал
def literal_str(name, deg):
    if deg:
       return name
    else:
       return '~' + name

# тестирование функции literal_str
#print(literal_str('A', 1))
#print(literal_str('B', 0))

# тестирование функции conj_str
#print(conj_str((0, 1, 0)))

# тестирование функции fdnf
print(fdnf(tt))

def xor_polynom(tt):
    polynom = []
    triangle = []
    tt_line = []
    for A in range(2):
        for B in range(2):
            for C in range(2):
                tt_line.append(tt[A, B, C])
    for A in range(2):
        for B in range(2):
            for C in range(2):
                if A == 0 and B == 0 and C == 0:
                    triangle.append(tt_line)
                else:
                    new_tt_line = []
                    for i in range(len(tt_line) - 1):
                        new_tt_line.append(tt_line[i] ^ tt_line[i+1])
                    tt_line = new_tt_line
                    triangle.append(tt_line)
    for line in triangle:
        print(line)
    i = 0
    for A in range(2):
        for B in range(2):
            for C in range(2):
                if triangle[i][0] == 1:
                    polynom.append([A, B, C])
                i += 1
    return polynom

def term_str(term):
    assert(len(term) == 3)
    vars = ['x', 'y', 'z']
    s = []
    for i in range(3):
        if term[i] == 0:
            continue
        elif term[i] == 1:
            s.append(vars[i])
    if s == []:
        return '1'
    else:
        return '&'.join(s)

def xor_polynom_str(polynom):
    return '0' if polynom == [] else ' ⊕ '.join(map(term_str, polynom))

polynom = xor_polynom(tt)
print(xor_polynom_str(polynom))
