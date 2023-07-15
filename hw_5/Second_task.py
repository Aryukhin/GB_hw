'''
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
'''

def gen_odd_num(n):
    res = (i for i in range(1, n + 1, 2))
    return res
test = gen_odd_num(10)

print(next(test))
print(next(test))
print(next(test))
