# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности в секундах:
#   a. до минуты в секундах
#   b. до часа в минутах и секундах
#   с. до суток в часах, минутах и секундах
#   d. * до месяца, до года, больше года

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
MONTH = DAY * 30.4167  # среднее количество дней в месяце равно примерно 30.4167
YEAR = DAY * 365.25  # среднее количество дней в году с учётом високосных равно 365.25

duration = int(input('Введите продолжительность промежутка времени в секундах: '))

if duration < MINUTE:
    print(f'Промежуток времени составляет: {duration} сек')
elif duration < HOUR:
    print(f'Промежуток времени составляет: {duration // MINUTE} мин '
          f'{duration % MINUTE} сек')
elif duration < DAY:
    print(f'Промежуток времени составляет:{duration // HOUR} час '
          f'{duration % HOUR // MINUTE} мин '
          f'{duration % HOUR % MINUTE} сек')
elif duration < MONTH:
    print(f'Промежуток времени составляет:{duration // DAY} дн '
          f'{duration % DAY // HOUR} час '
          f'{duration % DAY % HOUR // MINUTE} мин '
          f'{duration % DAY % HOUR % MINUTE} сек')
elif duration < YEAR:
    print(f'Промежуток времени составляет:{duration // MONTH:.0f} мес '
          f'{duration % MONTH // DAY:.0f} дн '
          f'{duration % MONTH % DAY // HOUR:.0f} час '
          f'{duration % MONTH % DAY % HOUR // MINUTE:.0f} мин '
          f'{duration % MONTH % DAY % HOUR % MINUTE:.0f} сек')
else:
    print(f'Промежуток времени составляет: {duration // YEAR:.0f} л '
          f'{duration % YEAR // MONTH:.0f} мес '
          f'{duration % YEAR % MONTH // DAY:.0f} дн '
          f'{duration % YEAR % MONTH % DAY // HOUR:.0f} час '
          f'{duration % YEAR % MONTH % DAY % HOUR // MINUTE:.0f} мин '
          f'{duration % YEAR % MONTH % DAY % HOUR % MINUTE:.0f} сек')

# Конечно, данное решение не совсем корректно, так как в месяцах на самом деле разное число дней,
# а ещё есть вискокосные года. В данном случае я просто взяла усреднённые значения.
# Но если требовалось именно понимание, как решать такого типа задачи,
# решение подойдёт, я думаю
