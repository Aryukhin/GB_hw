'''
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
'''

def gen_odd_nums(n):
    for res in range(1, n + 1, 2):
        yield res
print(*gen_odd_nums(100))