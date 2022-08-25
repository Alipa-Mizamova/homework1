GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
print(GeekTech)
del GeekTech['bag']
GeekTech['address'] = 'Ibraimova 103'
GeekTech['tel_nick'] = 'wa.me/996507052018 , @geektech_kg'
GeekTech['courses'].append('UI|UX')
GeekTech['courses'].append('IOS')
GeekTech['courses'] = set(GeekTech['courses'])
for key, value in GeekTech.items():
    print(f'{key}: {value}')
#
# print(GeekTech)