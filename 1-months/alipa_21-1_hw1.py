pr1 = input('Здравствуйте!!! Здесь вы можете вычислять '
            'среднего показателя температуры воздуха'
          'в Кыргызстане на сегодня.')
pr2 = input('Введите показатели температуры воздуха каждой области на сегодня.')
w1 = float(input('Бишкек '))
w2 = float(input('ОШ '))
w3 = float(input('Джалал-Абад '))
w4 = float(input('Баткен '))
w5 = float(input('Талас '))
w6 = float(input('Нарын '))
w7 = float(input('Ыссык-Көл '))
w8 = float(input('Чүй '))
sum_of_wh = w1+w2+w3+w4+w5+w6+w7+w8
average_wh = sum_of_wh / 8
rounded = round(average_wh,1)
print('Средний показатель температуры воздуха по КР на сегодня  ', rounded, '◦c')
print(type(rounded))