# Реализовать поиск простых чисел от 1 до 1 млн.
# Использовать простой алгоритм - перебором делителей до корня числа.
# Сделать это - без потоков, в потоках и в процессах. Произвести замеры времени для всех подходов.
import time
from math import sqrt
from datetime import datetime
from threading import Thread
import multiprocessing as mp


# ---------- без потоков ----------

def no_threading():
    start_time = datetime.now()
    result = []
    for i in range(3, 1_000_000):
        for j in result:
            if j > int((sqrt(i)) + 1):
                result.append(i)
                break
            if i % j == 0:
                break
        else:
            result.append(i)
    print(f'no multiprocessing: {datetime.now() - start_time}')
    return result


print(no_threading())


# ---------- в потоках ----------

def with_threading(n):
    start_time = datetime.now()
    result = []
    for i in range(3, n):
        for j in result:
            if j > int((sqrt(i)) + 1):
                result.append(i)
                break
            if i % j == 0:
                break
        else:
            result.append(i)
    print(f'with threading: {datetime.now() - start_time}')
    return ''


t = Thread(target=with_threading, args=(1_000_000,))
print(t.start())


# ---------- в процессах ----------

def with_multiprocessing(n):
    start_time = datetime.now()
    result = []
    for i in range(3, n):
        for j in result:
            if j > int((sqrt(i)) + 1):
                result.append(i)
                break
            if i % j == 0:
                break
        else:
            result.append(i)
    print(f'with multiprocessing: {datetime.now() - start_time}')
    return ''


if __name__ == '__main__':
    p = mp.Process(target=with_multiprocessing, args=(1_000_000,))
    p.start()
