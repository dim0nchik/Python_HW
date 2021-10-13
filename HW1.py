#№1
duration = int(input('Ведите время в секундах:'))

days = duration // (60*60*24)
hours = (duration - days * (60*60*24))//(60*60)
minutes = (duration - days * (60*60*24) - hours * (60*60)) //60
seconds = duration - days * (60*60*24) - hours * (60*60) - minutes * 60
print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

#№2
my_list = []
for num in range(1,1001,2):
    my_list.append(num ** 3)

final_sum = 0

for num in my_list:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 ==0:
        final_sum += num
print(final_sum)

final_sum = 0
for num in my_list:
    num += 17
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)


#№3
for number in range (1,101):
    if 4 < number % 100<= 20:
        print(f'{number} процентов')
    elif number % 10== 1:
        print(f'{number} процент')
    elif 1 < number % 10 < 5:
        print(f'{number} процента')
    else:
        print(f'{number} процентов')