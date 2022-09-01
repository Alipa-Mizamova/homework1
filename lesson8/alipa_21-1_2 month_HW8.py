# docs = open('docs.txt', 'w', encoding='UTF-8')
# docs.write('')
# docs.close()

with open('docs.txt', 'r', encoding='UTF-8') as docs:
    print(docs.read())