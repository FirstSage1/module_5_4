       # Модуль_5_4.py. Различие атрибутов класса и экземпляра.
       #============================================================
class House:                            # создание  класса
    houses_history = []                     # список названий созданных объектов


    def __new__(cls, *args, **kwargs):     #    создание экземпляра (объекта) класса
        cls.houses_history.append(args[0]) #ссылка на сам класс cls.Добавить название объекта в список cls.houses_history
        return object.__new__(cls)   # возврат экземпляра класса из базового класса object.

    def __init__(self, name, number_of_floors): #  атрибуты объекта
        self.name = name                          # доступ к атрибутам экземпляра
        self.number_of_floors = number_of_floors  # доступ к атрибутам экземпляра

    def __del__(self):          # удаление экземпляра
        print(f'Дом в {self.name} снесён, но он останется в истории')


#  Выполняемый код:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)             #печать(Класс дом.переменная-история домов)