from random import randint
number = randint(1, 101)
count = 0
min = 0
max = 100
print("Загадано число от 1 до 100")
print(f'программа рекомендует вам число:{round((max + min) / 2)}')
with open('alipa.txt', 'w', encoding='UTF-8') as file:
    file.write('Попытки: ')
while True:
    try:
        guess = int(input())
        count += 1
        if number == guess:
            break
        elif number > guess:
            min = guess
            print(guess, '<')
            print(f'программа рекомендует вам число:{round((max + min) / 2)}')
            with open('alipa.txt', 'a') as file:
                file.write(f'{guess} < {number}   \n')
        elif number < guess:
            max = guess
            print(guess, '>')
            print(f'Программа поиска рекомендует вам число:{round((max+min)/2)}')
            with open('alipa.txt', 'a') as file:
                file.write(f'{guess} > {number}   \n')
    except:
        print('Не корректный тип данных. Введите целое число! ')


print(f"Вы угадали число {number} за {count} попыток.")
with open('alipa.txt', 'a') as file:
               file.write(f'{guess} = {number}  \n')
with open('alipa.txt', 'r', encoding='UTF-8') as file:
    print(file.read())
