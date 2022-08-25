def first_word(text='Hello World'):
    if isinstance(text, str):
        return text.split()[0]
    else:
        return False
print(first_word('Mizamova Alipa'))
print(first_word())
print(first_word(123))


lst = [24, 19, 35, 46, 75, 29, 30, 18]

def calc_average(*lst):
    return  sum(lst)/len(lst)
print('averge= ', calc_average(int(sum(lst)/len(lst))))


def password_level(x):
    for i in x:
        if len(x) > 6 or i.isdigit() and i.isalpha():
            return True
        else:
            return False
print(password_level(input('введите пароль:  ')))

