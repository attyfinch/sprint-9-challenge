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


'''
Number of unique product names in the product list
Average (mean) price
Average (mean) weight
Average (mean) flammability

'''

def inventory_report(product_list):
    prod_count = 0
    total_price = 0
    total_weight = 0
    total_flammability = 0

    for prod in product_list:
        prod_count += 1
        total_price += prod.price
        total_weight = prod.weight
        total_flammability = prod.flammability
    
    return (prod_count, total_price/prod_count, total_weight/prod_count, total_flammability/prod_count)


if __name__ == '__main__':
    print(inventory_report(generate_products()))



