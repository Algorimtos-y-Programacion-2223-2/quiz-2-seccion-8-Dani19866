class Item:
    def __init__(self, id: int, name: str, type: str, stock: int, price: int):
        self.id = id
        self.name = name
        self.type = type
        self.stock = stock
        self.price = price
        
    def ShowInfo(self):
        print( f"ID: {self.id} | NAME: {self.name} | TYPE: {self.type} | STOCK: {self.stock} | PRICE: {self.price}" )
        
    def __str__(self) -> str:
        return f'ID: {self.id} | NAME: {self.name} | TYPE: {self.type} | STOCK: {self.stock} | PRICE: {self.price}'
    
class Tower:
    # def __init__(self, name: str, leves: int, street: str, city: str, postal: int, apaList: list):
    #     self.name = name
    #     self.levels = leves
    #     self.street = street
    #     self.city = city
    #     self.postal = postal
    #     self.apaList = []
        
    def __init__(self, **args):
        try:
            args = args['args'] 
            
            self.name = args["name"]
            self.levels = args["levels"]
            self.street = args["street"]
            self.city = args["city"]
            self.postal = args["postal"]
            self.apaList = args["apaList"]
        except KeyError:
            self.name = ""
            self.levels = 0
            self.street = ""
            self.city = ""
            self.postal = 0
            self.apaList = []
            
    def GetInformation(self):
        if self.name != "":
            print( f'[!] {self.street}, {self.city} {self.postal}' )
        else:
            print( f'[ERROR] Tower no created!' )
        
    def GetTypeTower(self):
        # Bloque residencial: (levels) x (6)
        if (self.levels * 6) < len( self.apaList ):
            print( '[%] Edificio tipo bloque residencial' )
        else:
            if self.name != "":
                print( '[%] Edificio tipo edificio residencial' )
            else:
                print( '[ERROR] Tower no created!' )
                
    def GetApartments(self):
        if len( self.apaList ) == 0:
            print( '[ERROR] This no have apartments!' )
        else:
            for apa in self.apaList:
                print(f"[#] {apa}")