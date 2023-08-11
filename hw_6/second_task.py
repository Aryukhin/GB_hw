"""
Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер
которых превышает объем ОЗУ компьютера.
"""
from collections import Counter
with open('result.txt', 'r', encoding='utf-8') as f:
    ip = []
    for line in f:
        line_1 = line.split("',")
        ip.append(line_1[0][2:])
    ans = Counter(ip).most_common(1)
    print(ans)
