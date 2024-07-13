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
        target_index = int(input("Введите номер элемента: "))
    except:
        print("Error")
        continue
    if target_index <= len(rez) and target_index > 0:
        item = rez[target_index - 1]
        if os.path.isfile(item):
            with open(item, 'r') as file:
                content = file.read()
                print(content)
    elif target_index == 0:
        print("Завершение работы...")
        break
    else:
        print("Введённый номер не соответствует количеству элементов списка")