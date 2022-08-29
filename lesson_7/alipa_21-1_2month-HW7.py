# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('')
# file.close()

with open('file.txt', 'r', encoding='UTF-8') as file:
    print(file.read())