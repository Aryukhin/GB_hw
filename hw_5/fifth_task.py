'''
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
'''
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
def unic_num(src):
    unic = set()
    basket = set()

    for i in src:
        if i not in basket:
            unic.add(i)
        else:
            unic.discard(i)
        basket.add(i)

    result = [el for el in src if el in unic]
    return result

print(unic_num(src))