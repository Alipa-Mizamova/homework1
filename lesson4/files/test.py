from file_executor.creat import creat_file
from file_executor.write import write_to_file
from file_executor.delete import delete_file
creat_file("adelia", '.txt')
write_to_file("adelia.txt", "Марлен")
delete_file("adelia.txt")


