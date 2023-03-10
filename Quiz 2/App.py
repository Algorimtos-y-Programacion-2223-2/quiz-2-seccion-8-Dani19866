from simple_colors import *
from Class import Item, Tower


class FirtsApp:
    def __Presentation(self):
        print( blue( "[+] EDIFICIOS + POO (IN PYTHON)" ) )
        
    def start(self):
        self.__Presentation()
        tower001 = Tower( args={ "name": "COTOPERI", "levels": 30, "street": "BUENAVENTURA", "city": "GUATIRE", "postal": 1221, "apaList": ["PISO 1 | APA 03 "] })
        tower001.GetInformation()
        tower001.GetTypeTower()
        tower001.GetApartments()
        
        tower002 = Tower()
        tower002.GetInformation()
        tower002.GetTypeTower()
        tower002.GetApartments()

class SecondApp:
    oldProducts = [
        {"id": 1, "name": "Nevera", "type": "Hogar", "stock": 753, "price": 800},
        {"id": 2, "name": "Cama", "type": "Hogar", "stock": 327, "price": 600},
        {"id": 3, "name": "Suéter", "type": "Ropa", "stock": 260, "price": 25},
        {"id": 4, "name": "Zapatos", "type": "Ropa", "stock": 593, "price": 5},
        {"id": 5, "name": "Laptop Gamer",
            "type": "Gaming", "stock": 11, "price": 2500},
        {"id": 6, "name": "Nintendo Switch OLED",
            "type": "Gaming", "stock": 25, "price": 400},
    ]
    newProducts = {
        "Hogar": [],
        "Gaming": [],
        "Ropa": []
    }

    def __Presentation(self):
        print(blue("[+] Tienda Súper Samancito"))
        print(blue(
            "[+] Menú de opciones de la tienda:\n      1: Ver productos\n      2: Salir del programa"))
        return input(cyan("[-] Opción a elegir: "))

    def __ResetStruct(self):
        for item in self.oldProducts:
            if item["type"] == "Hogar":
                self.newProducts["Hogar"].append(
                    Item(
                        id=item["id"],
                        name=item["name"],
                        type=item["type"],
                        stock=item["stock"],
                        price=item["price"]
                    )
                )

            if item["type"] == "Gaming":
                self.newProducts["Gaming"].append(
                    Item(
                        id=item["id"],
                        name=item["name"],
                        type=item["type"],
                        stock=item["stock"],
                        price=item["price"]
                    )
                )

            if item["type"] == "Ropa":
                self.newProducts["Ropa"].append(
                    Item(
                        id=item["id"],
                        name=item["name"],
                        type=item["type"],
                        stock=item["stock"],
                        price=item["price"]
                    )
                )

    def __ViewProducts(self):
        for brand in self.newProducts:
            for item in self.newProducts[brand]:
                print(item.__str__())

    def start(self):
        self.__ResetStruct()

        menuLoop = True
        while menuLoop:
            option = self.__Presentation()

            match option:
                case "1":
                    print()
                    self.__ViewProducts()
                    print()

                case "2":
                    print(green("[!] Cerrando programa..."))
                    menuLoop = False
                case _:
                    print(red("[ERROR] OPCIÓN ERRÓNEA"))
