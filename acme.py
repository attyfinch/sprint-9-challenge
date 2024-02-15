import random


class Product:
    def __init__(
            self, name,
            price=10,
            weight=20,
            flammability=0.5,
            identifier=random.randint(1000000, 9999999)
            ):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio < 1.0 and ratio >= 0.5:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        flame_level = self.flammability * self.weight
        if flame_level < 10:
            return "...fizzle."
        elif flame_level >= 10 and flame_level < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(
        self,
        name, price=10,
        weight=10,
        flammability=0.5,
        identifier=random.randint(1000000, 9999999)):
            super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"


if __name__ == '__main__':
    # prod_one = Product('soap')
    # prod_two = Product('soap', price=20, weight=100)
    # prod_three = Product('soap', price=20, weight=10)
    soap = Product('soap')
    print(soap.explode())

    soap.weight = 50
    print(soap.weight)

    glove = BoxingGlove('test', weight=50)
    print(glove.explode())
    print(glove.punch())
