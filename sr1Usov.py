class Item:
    def __init__(self, name, occupied_volume):
        self._name = name
        self._occupied_volume = occupied_volume

    @property
    def name(self):
        return self._name
    def check_item_volume(self):
        return self._occupied_volume

    def __str__(self):
        return self._name

class Bottle():
    def __init__(self, volume, level):
        #полный доступный объем бутылки в литрах
        self.volume = volume
        #сколько воды осталось в бутылке
        self.level = level

    def add_water(self, amount):
        if (amount + self.level) < self.volume:
            self.level += amount
        else:
            self.level = self.volume
        print(self)

    def drink_water(self, amount):
        if (self.level - amount) > 0:
            self.level -= amount
        else:
            self.level = 0
        print(self)
    def __str__(self):
        return f'Текущий уровень воды - {self.level}'

class Backpack:
    def __init__(self, volume):
        self._items = []
        #объем рюкзака в слотах
        self.volume = volume

    @property
    def items(self):
        return self._items

    def add_item(self, item):

        if self.volume - item.check_item_volume()>=0:
            self.volume -= item.check_item_volume()
            self._items.append(item)
            print(f'{item} добавлен в рюкзак')
        else:
            print(f'Не получается положить {item} в рюкзак, мало места')


    def check_backpack(self):
        print('Вещи в рюкзаке: ')
        for i in self._items:
            print(i, '')

class Tourist:
    class Tourist:
        def __init__(self):
            self._bottle = None
            self._backpack = None

    if __name__ == '__main__':
        item1 = Item('нож', 1)
        item2 = Item('палатка', 3)
        item3 = Item('пакет с документами', 1)
        item4 = Item('GPS трекер', 1)
        item5 = Item('Прата С++', 3)
        Eugene = Tourist()
        items = [item1, item2, item3, item4, item5]
        Eugene._backpack = Backpack(15)
        for i in items:
            Eugene._backpack.add_item(i)


        Eugene._bottle = Bottle(2.0, 2.0)

        while True:

            print("Выберите, что сделать туристу: 1 - попить воды, 2 - налить воды" )
            k = int(input("3 - проверить рюкзак, 4 - добавить новый предмет, 5 - уйти домой: "))

            if (k == 1):
                amount = float(input(("Сколько воды выпить: ")))
                Eugene._bottle.drink_water(amount)

            elif (k == 2):
                amount = float(input(("Сколько воды налить: ")))
                Eugene._bottle.add_water(amount)

            elif (k == 3):
                Eugene._backpack.check_backpack()

            elif (k == 4):
                name, volume = input("Введите название и объем предмета, который вы хотите добавить: ").split()
                item = Item(name, int(volume))
                Eugene._backpack.add_item(item)

            elif (k == 5):
                break
            else:
                print("Турист не знает такой команды")


<<<<<<< HEAD
print("Master push")

=======

print("testing git 0")
>>>>>>> testbranch1
