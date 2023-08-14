import sys
with open('bakery.csv', 'a', encoding='utf-8') as add:
    lenght = len(sys.argv[1])
    num = '0' * (8 - lenght) + sys.argv[1]
    add.write(num)
    add.write('\n')

