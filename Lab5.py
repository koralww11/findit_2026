class Sneakers:

    def __init__(self, brand, size, color, price, quantity, material, numberOfSales, etc):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.material = material
        self.numberOfSales = numberOfSales
        self.etc = etc



class SportShoesStore(Sneakers):

    def __init(self, brand, size, color, price, quantity, material, numberOfSales, etc, shop: list):
         
         super().__init__(brand, size, color, price, quantity, material, numberOfSales, etc)
         self.shop = shop


sneaker1 = Sneakers(
    brand="Nike",
    size=42.5,
    color="White",
    price=4500.0,
    quantity=15,
    material="Шкіра",
    numberOfSales=142,
    etc={"model": "Air Force 1 '07", "gender": "Unisex", "in_stock": True}
)


sneaker2 = Sneakers(
    brand="Adidas",
    size=41.0,
    color="Core Black",
    price=6200.0,
    quantity=8,
    material="Текстиль / Primeknit",
    numberOfSales=89,
    etc={"model": "Ultraboost Light", "purpose": "Running", "discount": 10}
)

sneaker3 = Sneakers(
    brand="New Balance",
    size=43.0,
    color="Grey",
    price=8900.0,
    quantity=3,
    material="Замша / Сітка",
    numberOfSales=210,
    etc={"model": "990v6", "country_of_origin": "USA", "limited_edition": True}
)

shop = [sneaker1, sneaker2, sneaker3]

shopp = SportShoesStore(shop)

print(shopp.shop)



    
