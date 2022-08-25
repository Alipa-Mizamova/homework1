while True:
    print("Выберите действие которое хотите сделать:\n"
          "Сложить: +\n"
          "Вычесть: -\n"
          "Умножить: *\n"
          "Поделить: /\n"
          "Выйти: q\n")

    action = input("Действие: ")

    if action == "q":
        print("Выход из программы")
        break
    try:
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
        y = float(input("y = "))
        if action == '+':
            print('%.2f + %.2f = %.1f' % (x, y, x + y))

        elif action == '-':
            print('%.2f - %.2f = %.1f' % (x, y, x - y))

        elif action == '*':
            print('%.2f * %.2f = %.1f' % (x, y, x * y))

        elif action == '/':
            if y != 0:
                print('%.2f / %.2f = %.2f' % (x, y, x / y))
            else:
                print("на ноль делить нельзя!")
    except:
        print('Не корректный тип данных. Введите целое или дробное число число! ')
