import os
import re

str = ''
for root, ds, fs in os.walk(f'./animalsAutoprompt_v15'):
    for f in fs:
        fullname = os.path.join(root, f)
        with open(fullname, 'r') as f:
            str+= f'{f.read()}\n'

with open('./animals.txt', 'w', encoding='utf-8') as f:
    f.write(str)
