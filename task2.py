# Реализовать решение задачи с подбором пароля для архива. Использовать потоки и процессы.
# Если будет желание можно попробовать свой вариант разделения задач по воркерам.
# Если нет - то можно использовать подход с очередью, генератором задач и исполнителями.

import itertools
import string
from datetime import datetime
from zipfile import ZipFile
from threading import Thread
import multiprocessing as mp

zip_object = ZipFile('lesson6.zip', 'r')


def generator(alphabet=string.ascii_lowercase):
    for pwd in itertools.product(alphabet, repeat=3):
        yield ''.join(pwd)


def final_password():
    start_time = datetime.now()
    for password in generator():
        try:
            zip_object.extractall(pwd=password.encode('utf-8'))
            print('PASSWORD FOUND: {}'.format(password))
            print(f'{datetime.now() - start_time}')
            break
        except Exception as e:
            continue


# --------------------Process----------------------

if __name__ == '__main__':
    print('Starting process')
    p = mp.Process(target=final_password)
    p.start()
    print('Done')

# --------------------Thread--------------------

t = Thread(target=final_password)
print('Starting thread')
print(t.start())
print('Done')


# Процесс работает быстрее
