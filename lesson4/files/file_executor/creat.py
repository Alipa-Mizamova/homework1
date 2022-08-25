import os
from pathlib import Path
def creat_file(file_name, extension):
    if os.path.isfile(file_name + extension):
        print('такой файл существует')

    else:
        with open(file_name + extension, 'w') as file:
            file.close()
    print(Path(file_name+extension).absolute())
