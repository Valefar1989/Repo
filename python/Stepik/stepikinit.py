class Laptop:
    def __init__(self, brand, model, price, bm=0):
        self.brand = brand
        self.model = model
        self.price = price
        self.bm = brand + " " + model


hp = Laptop("hp", "hp5555", 50000)
print(hp.bm)
