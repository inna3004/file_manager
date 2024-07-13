import os
import os.path


path = '.'

rez = sorted(os.listdir(path))
n: int
for n, item in enumerate(rez):
    print(n+1, item)

n_item =int(input("Введите номер элемента: "))

if n_item <= len(rez) and n_item > 0:
    item = rez[n_item - 1]
    if os.path.isfile(item):
        with open(item, 'r') as file:
            content = file.read()
            print(content)
elif n_item == 0:
    print("введеный номер не должен быть равен 0")
except ValueError:
    print("Введённый номер не является числом")
else:
    print("Введённый номер не соответствует количеству элементов списка")