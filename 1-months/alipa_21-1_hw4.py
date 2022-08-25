data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
# data_tuple = list(data_tuple)
print(data_tuple)
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1,2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[5] = 'T'
numbers[0] = numbers[0] ** 2
numbers[1] = numbers[1] ** 2
numbers[2] = numbers[2] ** 2
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)

