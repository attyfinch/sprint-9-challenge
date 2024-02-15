import random
import acme

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    for i in range(0, num_products):
        new_product = acme.Product(
            name=f'{random.choice(ADJECTIVES)} {random.choice(NOUNS)}',
            price=random.randint(5, 100),
            weight=random.randint(5, 100),
            flammability=random.uniform(0.0, 2.5))
        products.append(new_product)

    return products


def inventory_report(product_list):
    names_set = set()
    names = []
    prod_count = 0
    total_price = 0
    total_weight = 0
    total_flammability = 0

    for prod in product_list:
        names_set.add(prod.name)
        names.append(prod.name)
        prod_count += 1
        total_price += prod.price
        total_weight += prod.weight
        total_flammability += prod.flammability

    return (
        len(names_set),
        total_price/prod_count,
        total_weight/prod_count,
        total_flammability/prod_count
        )


# QA
if __name__ == '__main__':
    print(inventory_report(generate_products()))
