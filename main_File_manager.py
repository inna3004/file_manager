import os
import os.path
import sys


def get_dirlist(path="."):
    rez = sorted(os.listdir(path))
    return len(rez), rez


def print_list(dir_list):
    n: int
    for n, dir_item in enumerate(dir_list):
        print(n + 1, dir_item)


def user_input(max_size):
    target_index = 0
    while True:
        try:
            target_index = int(input(
                "Введите номер элемента, если хотите получить доступ к содержимому  папок и файлов каталога, иначе нажмите 0 для завершения работы программы: "))
            if max_size >= target_index > 0:
                return target_index
            if target_index == 0:
                print("Завершение работы...")
                sys.exit(0)
            else:
                print("Введённый номер не соответствует количеству элементов списка")
        except ValueError:
            print("Error")
            continue


def print_file(path):
    with open(path, 'r') as file:
        content = file.read()
        print(content)


max_elements, list_elements = get_dirlist()
print_list(list_elements)

dir_index = user_input(max_elements)

item = list_elements[dir_index - 1]
if os.path.isfile(item):
    print_file(item)
elif os.path.isdir(item):
    n, sub_items = get_dirlist(os.path.join(".", item))
    print("Содержимое каталога:")
    print_list(sub_items)
else:
    print("Это не файл и не папка")
