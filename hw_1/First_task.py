"""
### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 се
"""
duration = int(input())
days = duration // 86400
hours = (duration - 86400 * days) // 3600
mins = (duration - (86400 * days + hours * 3600)) // 60
sec = duration - (86400 * days + hours * 3600 + mins * 60)
print(days, "дн", hours , "час", mins, "мин", sec, "сек")

