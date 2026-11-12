class Printer:

    def __init__(self, name="None", speeddruk=0, price=0, weight=0, color="None"):
        self.__name = name
        self.__speeddruk = speeddruk
        self.__price = price
        self.weight = weight
        self.color = color


    def get_name(self):
        return f"Назва: {self.__name}"

    def get_speeddruk(self):
        return f"Швидкодія друку: {self.__speeddruk} ст/хв"

    def get_price(self):
        return f"Ціна: {self.__price} грн"

    def get_else(self):
        return f"Вага: {self.weight}, Колір = {self.color}"

    def __str__(self):
        return f"{self.__name}: {self.__speeddruk} ст/хв, {self.__price} грн"

    def __repr__(self):
        return f"Printer(name = {self.__name}, speed druk = {self.__speeddruk}, price = {self.__price}, weight = {self.weight}, color = {self.color})"
    
    def __del__(self):
        print(f"Принтер {self.__name} видалено")


    
def main():
    pr1 = Printer("HP", 12, 12000, 3, "White")
    pr2 = Printer("Canon", 15, 15000, 4, "Black")
    pr3 = Printer("Epson", 17, 20000, 7, "Red")
    pr4 = Printer()

    print("#1", 
        pr1.get_name(), 
        pr1.get_speeddruk(), 
        pr1.get_price(),
        pr1.get_else(), 
        pr1, 
        repr(pr1), sep = "\n")

    print("#2",
        pr2.get_name(), 
        pr2.get_speeddruk(), 
        pr2.get_price(),
        pr2.get_else(), 
        pr2, 
        repr(pr2), sep = "\n")

    print("#3",
        pr3.get_name(), 
        pr3.get_speeddruk(), 
        pr3.get_price(),
        pr3.get_else(), 
        pr3, 
        repr(pr3), sep = "\n")

    print("#4", 
            pr4.get_name(), 
            pr4.get_speeddruk(), 
            pr4.get_price(),
            pr4.get_else(), 
            pr4, 
            repr(pr4), sep = "\n")

    del pr1, pr2, pr3, pr4

if __name__ == "__main__":
    main()

