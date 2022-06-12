def game(n):
    assert type(n) is int
    assert n > 0

    i = 0
    c_prev = n
    while n > 0:
        user_number = i%2 + 1
        print(f'Uzytkownik nr: {user_number}')

        c = int(input('Podaj liczbę cukierków: '))

        if c > n or c <= 0:
            print('Podałeś złą liczbę cukierków. Podaj właściwą liczbę cukierków.')
            continue
        elif c > c_prev:
            print('Nie możesz wziąć więcej cukierków niż poprzedni gracz')
            print(f'Poprzedni gracz wziął {c_prev} cukierków')
            continue

        n -= c
        i += 1
        c_prev = c
        print(f'Zostało {n} cukierków')
    print('Koniec gry!')
    print(f'Wygrywa gracz nr {user_number}')

# game(1000)
#
# for i in range(5):
#     x = 10*i + i//5
#     print(x)
# else:
#     print('koniec')
#
# for i in range(5):
#     x = 10*i + i//5
#     if x > 20:
#         break
#     print(x)
# else:
#     print('koniec')
#
#
# # Stwórz listę liczb parzystych od 0 do 100,
# # wyszukaj w tej liście liczby podzielne zarówno przez 2 jak i 3
# # i każdą z takich liczb powiększ 100 razy, a zmodyfikowane liczby
# # umieść w liście w miejsce poprzednich
# # [0, 2, 4, 600, 8, ..]
#
# # sposob 1
# l = list(range(0, 101, 2))
# for i in range(len(l)):
#     if l[i] % 3 == 0:
#         l[i] *= 100
#
# print(l)
#
# # sposob 2
# l = list(range(0, 101, 2))
# for idx, el in enumerate(l):
#     if el % 3 == 0:
#         l[idx] *= 100
# print(l)
#
# # sposob 3
# lista = []
# for i in range(0,100,2):
#     if i%3==0:
#         z=i*100
#         lista.append(z)
#     else:
#         lista.append(i)
# print(lista)
#
# # sposob 4
# print('Nowy sposob')
# print([i*100 if i%3==0 else i for i in range(0, 100, 2)])
#
#
# s = 'Python jest moim ulubionym językiem programowania'
# s_list = s.split(' ')
#
# res = []
# for i in s_list:
#     i_len = len(i)
#     res.append(i_len)
#
# print(s_list)
# print(res)
#
# print([len(i) for i in s_list])
#
# print({len(i) for i in s_list})
#
# print([(i, len(i)) for i in s_list])
#
# print({i : len(i) for i in s_list})
#
# DATA = [
#     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
#     (5.8, 2.7, 5.1, 1.9, 'virginica'),
#     (5.1, 3.5, 1.4, 0.2, 'setosa'),
#     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
#     (6.3, 2.9, 5.6, 1.8, 'virginica'),
#     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
#     (4.7, 3.2, 1.3, 0.2, 'setosa'),
#     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
#
# # for i in DATA:
# #     print(i[0])
#
# print({i[4] for i in DATA[1:]})
# print(max([i[2] for i in DATA[1:]]))
#
# s = 'Python jest moim ulubionym językiem programowania'
# s_list = s.split(' ')
#
# res = []
# for i in s_list:
#     i_len = len(i)
#     if i_len > 6:
#         res.append(i_len)
#
# print(s_list)
# print(res)
#
# print([len(i) for i in s_list if len(i)>6])
# print([[i, len(i)] for i in s_list if len(i)>6])
# print({i : len(i) for i in s_list if len(i)>6})
#
# print(min([i[2] for i in DATA[1:] if i[-1] == 'setosa']))
#
# print([f'{i} parzysta' if i%2==0 else f'{i} nieparzysta' for i in range(10)])
#
# print((len(i) for i in s_list))
#
# gen = (len(i) for i in s_list)
# #print([i for i in gen])
#
# print(next(gen))
# print(next(gen))
#
# print(tuple(len(i) for i in s_list))
# print(list(len(i) for i in s_list))
#
#
# print(any([True, False, True, True, True]))
# print(all([True, False, True, True, True]))
#
# print(any([i%5==0 for i in range(11)]))
#
# ####### FUNKCJE ######
#
# def l_stats(l):
#     l_max = max(l)
#     l_min = min(l)
#     l_len = len(l)
#     l_mean = sum(l)/l_len
#     return (l_max, l_min, l_len, l_mean)
#
# print(l_stats([-2, 3, 5, 7]))
#
# a, b, c, d = l_stats([-2, 3, 5, 7])
# print(a, b, c, d)
#
# a, b, c, _ = l_stats([-2, 3, 5, 7])
#
# l = [[1, 3, 'x'],
#      [2, 4, 'x'],
#      [1, 5, 'x']]
# for el1, el2, el3 in l:
#     print(el1, el2, el3)
#
# l = [[1, 3, 'x'],
#      [2, 4, 'x'],
#      [1, 5, 'x']]
# for el1, el2, _ in l:
#     print(el1, el2, el3)
#
# a, b, _, _ = l_stats([-2, 3, 5, 7])
# print(a, b)
#
# a, b, *c = [1, 5, 5, 6, 7, 7, 3, 7]
# print(a, b, c)
#
# *a, b = [1, 5, 5, 6, 7, 7, 3, 7]
# print(a, b)
#
# a, *b, c = [1, 5, 5, 6, 7, 7, 3, 7]
# print(a, b, c)
#
# # a, *b, c = [1]
# # print(a, b, c)
#
# a, *b, c = [1, 2]
# print(a, b, c)
#
# a, *_, c = [1, 5, 5, 6, 7, 7, 3, 7]
# print(a, c)
#
# def list_mult(l, m):
#     return l*m
#
# print(list_mult([1, 2, 3], 5))
#
# # list_mult([1, 3, 4], 8, 6)
#
# def list_mult(l, m=3):
#     return l*m
#
# print(list_mult([1, 2, 3], 5))
# print(list_mult([1, 2, 3]))
#
# # def list_mult(m, l=[1, 3], r):
# #     return l*m*r
#
# def shopping_list(*args):
#     for a in args:
#         print(a)
#
# shopping_list('mleko', 'chleb')
# shopping_list()
#
# def shopping_list(d, *args):
#     print(d)
#     for a in args:
#         print(a)
#
# shopping_list('wtorek', 'mleko', 'chleb')
# shopping_list('wtorek')
#
#
# def norm(p, *args):
#     res = 0
#     for i in args:
#         res += pow(abs(i), p)
#     return pow(res, 1/p)
# print(norm(2, 1, 3, 4, 5))
#
#
# def list_mult(l, m):
#     return l*m
#
# print(list_mult(m=3, l=[1, 3, 4]))
#
#
# def trip(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k} ma {v} lat')
#
# trip(ala=5, kasia=3)
#
# def trip(x, **kwargs):
#     print(x)
#     for k, v in kwargs.items():
#         print(f'{k} ma {v} lat')
#
# trip('wycieczka', ala=5, kasia=3)
#
# def shopping_cost(**kwargs):
#     print(kwargs.keys())
#     return sum(kwargs.values())
#
# print(shopping_cost(p1=30, p2=4, p3=5))
#
# l123 = 10
#
# def f(n):
#     x123 = 2*n*l123
#     return x123
#
# print(f(4))
#
# def f(n):
#     global l123
#     l123 = 100
#     x123 = 2*n*l123
#     return x123
#
# print(f(4))
# print(l123)
#
# def square(x):
#     return x ** 2
#
# print(square(5))
#
# res = map(square, [1, 2, 3])
# print(list(res))
#
# # lambda x: x+1
# # lambda x, y: x+y
#
# def f(x):
#     return x+1
#
# def f1(x, y):
#     return x+y
#
# # f = lambda x: (14*x-6)**2
#
# res = map(lambda x: (14*x-6)**2, [1, 2, 3])
# print(list(res))
#
# # Wykorzystując funkcje lambda oblicz ile liczb od 1 do 100 jest podzielnych przez 2
#
# print(sum(list(map(lambda x: x%2 == 0, list(range(1, 101))))))
#
# # 3! = 3*2*1 = 3 * 2!
#
# def f(n):
#     res = 1
#     for m in list(range(2, n+1)):
#         res *= m
#     return res
#
# print(f(3))
#
# def f1(n):
#     if n == 0: return 1
#     else: return n*f1(n-1)
#
# print(f1(3))
#
# # a_0 = 0
# # a_1 = 1
# # a_n = a_(n-1) + a_(n-2)
#
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(13))



# raise RuntimeError('błąd!')

t = -10

# if t >= 0:
#     print('temperatura jest ok')
# else:
#     raise ValueError

def check(t):
    if type(t) not in {float, int}:
        raise TypeError('Temperatura musi być liczbą')
    if t < 0:
        raise ValueError('Temperatura w K nie może być ujemna')
    return t

# check('-10')

def check(a):
    if not isinstance(a, int):
        raise TypeError('Wiek musi być liczbą całkowitą')
    if a < 0:
        raise ValueError('Wiek nie może być ujemny')
    return t

# check('a')

# name = 'Jonh'
# name.append('xxx')
#
# l = [1, 2, 3]
# l[100]

# open(r'C:\\folder1\\folder1\\plik.txt') <- scieżka bezwzględna
# open('plik.txt') # <- scieżka względna

# import detectron2
#
# d = {1: 'a', 2: 'b'}
# d[5]
#
# print(xxxxxxxxx)
#
# if x==1
#     print('')
#
# 3 + 'c'
#
# a, b, c = [1, 2]

a = 1
b = 0

# try:
#     a/b
# except ZeroDivisionError:
#     print('nie mozna dzielic przez 0!')
#
# try:
#     a/b
# except ZeroDivisionError as error:
#     print('nie mozna dzielic przez 0!')
#     print(error)
#
#
def connect():
    raise ConnectionError('Nie można się połączyć z bazą danych')

try:
    connect()
except ConnectionRefusedError:
    print('Connection Refused')
except ConnectionResetError:
    print('Connection Reset')
except ConnectionError:
    print('blad')
#
# def connect():
#     #pass
#     raise ConnectionError('Nie można się połączyć z bazą danych')
#
# try:
#     connect()
# except (ConnectionRefusedError, ConnectionResetError):
#     print('Connection Refused')
# except ConnectionError:
#     print('blad')
# else:
#     print('połaczenie udane')
# finally:
#     print('połączenie zamknięte')
#
# try:
#     l[10000]
# except:
#     print('jakis blad')
#
# try:
#     l[10000]
# except Exception as e:
#     print('jakis blad')
#     print(e)
#
# # try:
# #     l[10000]
# # except ConnectionRefusedError:
# #     print('jakis blad')
# #     print(e)
#
#
# def convert(d):
#     try:
#         d_conv = int(d)
#     except ValueError:
#         print('niepoprawna wartość')
#         d_conv = None
#     except TypeError:
#         print('niepoprawny typ')
#         d_conv = None
#     finally:
#         print(d)
#     return d_conv
#
# convert(print)
#
# l = [1, 2, 3]
# # assert 5 in l, '5 musi być w liście'
# assert type(l) is list
# assert all(type(i) is int for i in l)
#
# l = [42, 50, 45, 10, 100]
# for i in l:
#     assert i <= 50, 'Przekroczenie predkosci'
#     print(f'{i} jest OK')
