# #№1
# print(type(15 * 3))
# print(type(15 / 3))
# print(type(15 // 2))
# print(type(15 ** 2))
# #№2
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# new_list = []
# for elen in my_list:
#     if elen.isdigit():
#         new_list.extend(['"', f'{int(elen):02}', '"'])
#     elif (elen.startswith('+") or elen.starswith ("-')) and elen[1:].isdigit():
#         new_list.extend(['"', f'{elen[0]}{int(elen[1:]):02}', '"'])
#     else:
#         new_list.append(elen)
# out_info = ' '.join(new_list)
# print(out_info)
#№3
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# idx = 0
# while idx < len(my_list):
#     if my_list[idx].isdigit():
#         my_list.insert(idx, '"')
#         my_list[idx + 1] = f'{int(my_list[idx + 1]):02}'
#         my_list.insert(idx + 2, '"')
#         idx += 2
#     elif (my_list[idx].startswith('+') or my_list[idx].startswith('-')) and my_list[idx][1:].isdigit() :
#
#         my_list.insert(idx, '"')
#         my_list[idx + 1] = f'{my_list[idx + 1][0]}{int(my_list[idx + 1]):02}'
#         my_list.insert(idx + 2, '"')
#         idx += 2
#     idx += 1
#
# out_info = ' '.join(my_list)
# print(out_info)
#№4
# bad_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# for position in bad_list:
#     print('Привет', position.split()[-1].title())
#№5
# rate = [57.8,46.51,97,18,22.40,21.32,43.50,69.54,666.66,109.12]
# for good in rate:
#     rub = int(good)
#     kk = (good - int(good)) * 100
#     print(f'{rub} руб {kk:02.0f} коп')