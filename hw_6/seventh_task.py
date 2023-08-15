'''
*(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
которой не существует.
'''

import sys
with open('bakery.csv', 'r+', encoding='utf-8') as edit:
    if int(sys.argv[1]) > len(edit.readlines()):
        print(f'list out of range')
    else:
        edit.seek((int(sys.argv[1]) - 1) * 10)
        num = '0' * (8 - len(sys.argv[2])) + sys.argv[2]
        edit.write(num)

