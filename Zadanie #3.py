import numpy

q = 20
ar = numpy.random.randint(-15, 15, q) # создание массива
max_abs = -16 # переменная для хранения максимального значения массива
count = 0 # считает количество элементов по модулю больших, чем максимальный


for i in range(q): # Перебор элементов массива.
    # Если значение элемента больше переменной max_abs - значение переменной заменяется текущим значением элемента
    if ar[i] > max_abs:
        max_abs = ar[i]

for i in range(q):
    if abs(ar[i]) > (max_abs):
        count += 1
print(ar)
print(count)