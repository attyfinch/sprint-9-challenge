import random
import acme

'''
name should consist of a random adjective from the list: ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'] followed by a space and then a random noun from the list: ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???'], e.g. 'Awesome Anvil' and 'Portable Catapult' are both potential names that could be generated

price and weight should both be random integers from 5 to 100 (inclusive)

flammability should be a float ranging from 0.0 to 2.5 (inclusive)
'''

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


# should randomly generate a given number of products (default 30), and return them as a list
def generate_products(num_products=30):
    products = []

    for i in range(0, num_products):
        new_product = acme.Product(
            name=f'{random.choice(adj)} {random.choice(noun)}', 
            price=random.randint(5, 100),
            weight=random.randint(5, 100),
            flammability=random.uniform(0.0, 2.5))
        # print(new_product.name, new_product.price, new_product.weight, new_product.flammability)
        products.append(new_product)        

    return products

if __name__ == '__main__':
    print(generate_products())



