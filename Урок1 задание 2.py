sec = int(input('Введите время в секундах: '))
hour = sec // 3600
minute = (sec - (hour * 3600)) // 60
sec1 = (sec - (hour * 3600)) - (minute * 60)
if 0 <= hour < 10:
    hour = str(0) + str(hour)
if 0 <= minute < 10:
    minute = str(0) + str(minute)
if 0 <= sec1 < 10:
    sec1 = str(0) + str(sec1)
print(hour, 'ч:', minute, 'м:', sec1, 'с')
