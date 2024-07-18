import os
import os.path

# TODO: Добавить примечания для пользователя
# TODO: Сделать просмотр содержимого папок


path = '.'

while True:
    rez = sorted(os.listdir(path))
    n: int
    for n, item in enumerate(rez):
        print(n+1, item)
    target_index = 0

    try:
        target_index = int(input("Введите номер элемента, если хотите получить доступ к содержимому  папок и файлов каталога, иначе нажмите 0 для завершения работы программы: "))
    except:
        print("Error")
        continue
    if target_index <= len(rez) and target_index > 0:
        item = rez[target_index - 1]
        if os.path.isfile(item):
            with open(item, 'r') as file:
                content = file.read()
                print(content)
        elif os.path.isdir(item):
            sub_items = os.listdir(os.path.join(path, item))
            print("Содержимое каталога:")
            for sub_n, sub_item in enumerate(sub_items):
                print(f"{sub_n + 1} {sub_item}")
        else:
            print("Это не файл и не папка")
    elif target_index == 0:
        print("Завершение работы...")
        break
    else:
        print("Введённый номер не соответствует количеству элементов списка")