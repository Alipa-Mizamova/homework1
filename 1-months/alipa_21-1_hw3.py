eng_vowels = "eyuioaEYUIOA"
rus_vowels = "аоуыиеёэюяУЕЭОАЫЯИЮ"
eng_consonants = "wrtpsdfghjklzxcvbnmQWRTPLKJHGFDSZXCVBNM"
rus_consonants = "цкнгшщзхждлрпвфчмтбЦЙУКНГШЩЗХЖДЛРПВФЧСМТБ"
rus_sign = "ъь"
while True:
    word = input('\nвведите слово: ')
    print('количество букв: ', len(word))
    if word == 'exit':
        print('программа завершена!')
        break

    eng_v = 0
    for i in word:
        if i in eng_vowels:
            eng_v += 1
    print('eng_vowels: ',eng_v)

    eng_c = 0
    for i in word:
        if i in eng_consonants:
            eng_c += 1
    print('eng_consonants:',eng_c)

    rus_v = 0
    for i in word:
        if i in rus_vowels:
            rus_v += 1
    print('rus_vowels: ', rus_v)

    rus_c = 0
    for i in word:
        if i in rus_consonants:
            rus_c += 1
    print('rus_consonants: ', rus_c)

    rus_s = 0
    for i in word:
        if i in rus_sign:
            rus_s += 1
    print('rus_sign : ', rus_s)

    eng_v = (round(eng_v / len(word) * 100, 2))
    print("eng_vowels/Eng_consonants", int(eng_v), '%', '/', round(int(eng_c )/ len(word) * 100, 2), '%')

    rus_v = (round(rus_v / len(word) * 100, 2))
    print("Гласные/Согласные", float(rus_v), '%', '/', round(float(rus_c) / len(word) * 100, 2), '%')

    # rus_s = (round(rus_v / len(word) * 100, 2))
    print("русские знаки",  round(float(rus_s) / len(word) * 100, 2), '%')

