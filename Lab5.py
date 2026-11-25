class Sneakers

    def __init__(self, brand=None, size=0, color=None, price=0,
                 quantity=0, material=None, numberOfSales=0, etc=None):
        self.brand = brand
        self.size = size
        self.color = color
        self.material = material
        self.etc = etc
        self.price = price
        self.quantity = quantity
        self.numofsale = numberOfSales

    def __str__(self):
        return (f"{self.brand}: Ціна: {self.__price}, Розмір: {self.size}, "
                f"Колір: {self.color}, Кількість: {self.__quantity}")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if val < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self.__price = val

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, val):
        if val < 0:
            raise ValueError("Кількість не може бути від'ємною")
        self.__quantity = val

    @property
    def numofsale(self):
        return self.__numberOfSales

    @numofsale.setter
    def numofsale(self, val):
        if val < 0:
            raise ValueError("Кількість продажів не може бути від'ємною")
        self.__numberOfSales = val


class SportShoesStore:

    def __init__(self):
        self.__store = []

    def add(self, shoe):
        self.__store.append(shoe)

    def remove(self, shoe):
        if shoe in self.__store:
            self.__store.remove(shoe)
            print(f"Кросівки {shoe.brand} видалено з магазину")
        else:
            print("Таких кросівок немає в магазині")

    def sort_price(self):
        return sorted(self.__store, key=lambda shoe: shoe.price)

    def sort_quantity(self):
        return sorted(self.__store, key=lambda shoe: shoe.quantity)

    def sort_popular(self):
        return sorted(self.__store, key=lambda shoe: shoe.numofsale, reverse=True)

    def __str__(self):
        if not self.__store:
            return "Магазин порожній"

        lines = ["Кросівки в наявності:"]
        lines.extend(str(shoe) for shoe in self.__store)
        return "\n".join(lines)


def main():
    shoes1 = Sneakers("Nike", 42, "Чорний", 3500, 15, "Шкіра", 120, "Амортизація Air")
    shoes2 = Sneakers("Adidas", 40, "Білий", 2000, 25, "Текстиль", 340, "Для бігу")
    shoes3 = Sneakers("Puma", 45, "Зелений", 1200, 14, "Синтетика", 360, "Легка підошва")
    shoes4 = Sneakers("Asics", 41, "Синій", 4100, 32, "Синтетика", 230, "Для залу")

    shoesstore = SportShoesStore()
    for shoe in (shoes1, shoes2, shoes3, shoes4):
        shoesstore.add(shoe)

    print("Рейтинг за ціною")
    for shoe in shoesstore.sort_price():
        print(shoe)

    print("\nРейтинг за кількістю")
    for shoe in shoesstore.sort_quantity():
        print(shoe)

    print("\nТоп найпопулярніших")
    for shoe in shoesstore.sort_popular():
        print(shoe)

    print()
    print(shoesstore)

    print()
    shoesstore.remove(shoes1)
    print(shoesstore)


if __name__ == "__main__":
    main()
