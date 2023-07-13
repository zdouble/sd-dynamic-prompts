import os
import re

str = ''
for root, ds, fs in os.walk(f'./clothing'):
    for f in fs:
        fullname = os.path.join(root, f)
        s = re.sub(r'\.txt', '__', fullname)
        s = re.sub(r'\.\/', '__', s)
        s = re.sub(r'\\', '/', s)
        str += f'{s}\n'

with open('./all.txt', 'w', encoding='utf-8') as f:
    f.write(str)
