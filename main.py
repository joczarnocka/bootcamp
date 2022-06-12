# paulina.grudzinska26@gmail.com

print('hello')

age = 5
print(age)

# print = 3

age1 = 'mam 5 lat'
print(age1)

my_age = 10 # myAge

HOUR = 60

number_of_hours = 8

number_of_min = number_of_hours * HOUR
print(number_of_min)

# zmienne calkowite
a = 3
b = -2

print(a + b)
print(a - b)
print(a * b)
print(a/b)

print(1+3)

# liczby zmiennoprzecinkowe
c = 1.0 # 1.
d = 5.1
e = 0.5 # .5

f = 2_223_345_567
print(f)

g = 1e3
h = 3e-6

print(g)
print(h)

# dzielenie
print(10/3)
print(10//3) # dzielenie calkowite
print(10%3) # dzielenie modulo (reszta z dzielenia)

print(2**5)
print(2**(1/2))

print(pow(2, 3))
print(abs(-4))

# - zadeklaruj dwie zmienne przechowujące informacje o długości boków prostokąta w centymetrach
# i przypisz im dowolne dodatnie wartości
# - oblicz długość przekątnej prostokąta w całkowitych metrach (twierdzenie Pitagorasa)

x1 = 500
x2 = 7_000

res = ((x1**2 + x2**2) ** (1/2)) // 100
print(res)

print(a)
a = a + 1
print(a)
a += 1
print(a)

a -= 1
print(a)

a *= 2
print(a)

print(type(a))
print(type(d))

print(isinstance(-3, int))
print(isinstance(-3, float))

print(type(int))

print(float(3))
print(int(3.0))
print(int(3.2))
print(int(3.7))

print(round(3.7))
print(round(3.77777, 3))

# zmienne logiczne
x = True
# x = TRUE
y = False

print(x)
print(type(x))

print(bool(0))
print(bool(1))

print(bool(3))
print(bool(-3))

print(float(True))

print(x + y)

print(x | y) # lub
print(x & y) # i

x = 2 # operator przypisania
print(1 == 2) # operator porownania

print(1 != 2)

print(1 > 2)
print(1 >= 2)
print(1 < 2)
print(1 <= 2)

print((x == 1) or (x == 2))
print( x == 1 and x == 2)

print(not x == 3)
print(not False)

# None to brak
x = None
print(type(x))
print(x is None)
print(None is False)

# stringi
s = 'abc'
print(s)
print("abc")

s = """
a
b
c
"""
print(s)
print('a\nb\nc')
print('a\tb')

s = '1'
print(type(int(s)))

print(float('-1.2')) # print(float('1,2')) <- zle

print('1' + '2')
print('a'*5)

age = 5
s = 'Mam age lat'
print(s)

age = 15
s = f'Mam {age} lat'
print(s)

s = 'Mam {} lat'.format(age)
print(s)

# x = int(input('Podaj wiek: '))
# print(x)
# print(type(x))
#
# x = input('Podaj imię: ')
# print(x)
# print(type(x))

### Zadanie 2
# Zapytaj użytkownika o poniższe zmienne (zadbaj o odpowiednie typy):
# - imię
# - wiek
# - wzrost (w metrach)
# - czy uczysz się Pythona
#
# Następnie ułóż te informacje w słowny opis używając f-stringa.
# Każda informacja powinna znajdować się w oddzielnej linijce.

# name = input('Imię: ')
# age = int(input('Wiek: '))
# height = float(input('Wzrost [m]: '))
# learning_python = bool(int(input('Czy uczysz się pythona? ')))
#
# res = f"""
# Mam na imię {name}
# Mam {age} lat
# Mam {height}m wzrostu
# Czy uczę się pythona? {learning_python}
# """
# print(res)

# print(bool(''))


s = 'abcdef'
print(len(s))

print(s[1])
print(s[0])
print(s[len(s)-1])
print(s[-1])
print(s[2:4])
print(s[2:])
print(s[::2])
print(s[::-1])

s = '  a b c d e '
s = s.upper()
print(s)
print(s.replace('A', 'x'))
print(s.find('G'))

print(s.count(' '))
print(s.strip())
print(s.lstrip())
print(s.strip().capitalize())
print(s.strip()\
       .capitalize()\
       .startswith('A'))

s = """
 os. Jana III sobieskiego
ul. Jana III Sobieskiego
ul Jana III Sobieskiego
  ul.Jana III  Sobieskiego
ulicaJana III Sobieskiego
Ul. Jana III Sobieskiego
UL. Jana   III sobieskiego
 ulica Jana Iii Sobieskiego
Ulica. Jana   Ill Sobieskiego
"""

t = s.upper()\
    .replace('   ', '')\
    .strip()\
    .replace('  ', '')\
    .replace('OS', 'UL')\
    .replace('ULICA', 'UL')\
    .replace('UL ', 'UL.')\
    .replace(' UL', 'UL')\
    .replace('UL.J', 'UL. J')\
    .replace('ULJ', 'UL. J')\
    .replace('ILL','III')

print(t.count('UL. JANA III SOBIESKIEGO'))

t_list = t.split('\n')
print(t_list)
print(type(t.split('\n')))
print(', '.join(t_list))

s = """
 os. Jana III sobieskiego
ul. Jana III Sobieskiego
ul Jana III Sobieskiego
  ul.Jana III  Sobieskiego
ulicaJana III Sobieskiego
Ul. Jana III Sobieskiego
UL. Jana   III sobieskiego
 ulica Jana Iii Sobieskiego
Ulica. Jana   Ill Sobieskiego
"""

print(' '.join(s.split()))

l = []  # list()
print(l)
print(bool([]))
print([1, 2, 'aaa'])
l.append(1)
print(l)
l.append(-5)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l = l + [1, 2]
print(l)
print(l.count(1))
print(l[0])
print(l[1:])
l.reverse()
print(l)
print(sum(l))
print(min(l))
del l[0]
print(l)
l[0] = 2*l[0]
print(l)

t = (1, 2, 3)
print(type(t))
t1 = (1, )
print(type(t1))
print(len(t))
print(max(t))
# t[0] = 3

# Trzy razy poproś użytkownika o podanie liczby. Każdą z liczb dodaj do listy.
# Posortuj listę i oblicz sumę jej elementów.

# e1 = float(input('Podaj liczbę: '))
# e2 = float(input('Podaj liczbę: '))
# e3 = float(input('Podaj liczbę: '))
#
# l = [] # l = [e1, e2, e3]
# l.append(e1)
# l.append(e2)
# l.append(e3)
# l.sort()
# print(l)
# print(sum(l))

s = {1, 3, 5}
print(s)
print(len(s))
print(max(s))

s1 = {1, 2, 3}
s2 = {1, 'abc'}
print(s1 - s2)
print(s1.intersection(s2))
s1.add('def')
print(s1)
s1.pop()
print(s1)
print(s1.issubset(s2))

print(list(s1))
print([s1])
print(set([1, 3]))

l = [
    [1, 2, 3],
    {1, 5, 7},
    (0, 'k', ['a', 1])
]
print(l[0][1])

d = {1: 'a', 2: 'b', 'k': {1, 3}}
print(d)
print(d.keys())
print(d.values())
print(d.items())
d[3] = 'c'
print(d)
d[1] = 'c'
print(d)
print(d.get(1))
print(d.get(11))
print(d[1])
# print(d[11])

del d[1]
print(d)

new = {'m' : 1}
d.update(new)
print(d)

print(set([1, 1, 1]))

# kopiowanie plytkie
a = ['red', 'blue', 'pink']
b = a

a.append('black')
print(a)
print(b)


print(id(a))
print(id(b))

# kopiowanie glebokie
a = ['red', 'blue', 'pink']
b = a.copy()

a.append('black')
print(a)
print(b)

print(id(a))
print(id(b))



x = 5
# print(x < 0)
# if x < 0:
#     print('liczba jest ujemna')
# else:
#     print('liczba NIE jest ujemna')

x = 5
print(x < 0)
if x < 0:
    print('liczba jest ujemna')
else: print('liczba NIE jest ujemna')

x = -26
if x < 0 and x%13 == 0:
    print('liczba ujemna podzielna przez 13')
elif x < 0:
    print('liczba ujemna')
elif x > 0:
    print('liczba dodatnia')
else:
    print('zero')

x = -13
if x < 0:
    print('if nr 1')
    if x%13==0:
        print('if nr 2')
        print('liczba ujemna podzielna przez 13')
    else:
        print('liczba ujemna')
elif x > 0:
    print('liczba dodatnia')
else:
    print('zero')

if []:
    print('lista')
else:
    print('pusta lista')

if 1 in [1, 3, 5]:
    print('jest!')
else:
    print('nie ma')

### Zadanie 5
# Napisz instrukcję warunkową, która sprawdzi, do której klasy należy podane słowo:
# - jeśli słowo ma długość < 10 -> krótkie słowo
# - jeśli słowo ma długość >= 10 i dzielenie całkowite długości słowa przez 1/3 równa 0 -> pechowe słowo
# - jeśli słowo ma długość >= 10 i zawiera co najmniej 3 litery 'a' -> aaa słowo
# - w przeciwnym przypadku -> długie słowo

s = 'trzynaaaascie'
if len(s) < 10:
    print('krótkie słowo')
elif len(s) >= 10:
    if len(s)%13 == 0:
        print('pechowe słowo')

    if s.count('a') >= 3:
        print('aaa')
    else:
        print('długie słowo')

i = 0
while i < 5:
    print(i)
    i += 1

print('')

i = 0
while i <= 30:
    print(i)
    if i < 10:
        i += 5
    else:
        i += 10

print('')
for i in [1, 3, 4]:
    print(i)

for i in {23, 34, 14, 33}:
    if i % 3 == 0:
        print(f'{i} jest podzielna przez 3')
    else:
        print(i)

print(d)
for i in d:
    print(i)
print('')
for i in d.values():
    print(i)

print()
for i in range(1, 100, 5):
    print(i)

c = 0
for i in range(1_000_000):
    print(i)
    if i % 5 == 0:
        print(f'{i} jest podzielne przez 5')
        c += 1
    if c == 5:
        break

for i in range(10):
    if i%2 == 0:
        continue
    else:
        print(i)

print()
for i in range(10):
    if i%2 == 0:
        print(f'{i} jest podzielna przez 2')
        continue
    print(i)

for i in [1, 3, 4]:
    pass

for i in [-3, 5, 7]:
    for j in [-1, -3, 4]:
        ij = i*j
        if i < 0 and j < 0:
            print(f'({i})*({j})= {ij}')
        elif i < 0 and j >= 0:
            print(f'({i})*{j}= {ij}')
        elif i >= 0 and j < 0:
            print(f'{i}*({j})= {ij}')
        else:
            print(f'{i}*{j}= {ij}')


for i in [-3, 5, 7]:
    for j in [-1, -3, 4]:
        s = str(i)
        if i < 0:
            s = f'({i})'
        if j >= 0:
            s = s + f'*{j}'
        else:
            s = s + f'*({j})'
        ij = i*j
        s = s + f'={ij}'
        print(s)

for i, j in zip([1, 3, 4], [2, 3, 4]):
    ij = i + j
    print(f'{i}+{j}={ij}')

for idx, i in enumerate(['raz', 'dwa', 'trzy']):
    print(f'{idx}: {i}')

s = 'kajak'
res = True
for i in range(len(s)//2):
    if s[i] != s[-1-i]:
        print('nie jest palindromem')
        res = False
        break
if res:
    print('jest palindromem')

# s == s[::-1]
# s == s.reverse()


def say_hello():
    print('hello')

print(say_hello())

def say_hello_2():
    return 'hello 2'

hello_res = say_hello_2()
print(hello_res)

def hello():
    if False:
        print('before')
        return 'hello'
    else:
        print('xxx')
        return 'world'
        print('after')

print(hello())

def hello(name):
    return f"hello {name}"

print(hello('Adam'))

def round_sum(a, b):
    u = round(a + b)
    return u

print(round_sum(2.5, 4))
# print(u)

def my_function(arg1):
    """
    Summary line.

    Extended description of function.

    Parameters:
    arg1 (type): Description of arg1

    Returns:
    ret1 (type): Description of return value

    """
    ret1 = 2 * arg1

    return ret1


print(my_function.__doc__)

def len_diag(x1, x2):
    return ((x1**2 + x2**2) ** (1/2)) // 100

print(len_diag(100, 230))

