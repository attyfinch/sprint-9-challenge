from acme import Product
from acme_report import generate_products


def test_default_product_price():
    '''Test default Product values return correct values'''
    prod = Product('Test Product')
    assert prod.price == 10
    assert prod.weight == 20
    assert prod.flammability == 0.5


def test_takes_new_inputs():
    '''Test custom inputs for Product return correct values'''
    prod = Product('Test Product', price=12, weight=15, flammability=20)
    assert prod.price == 12
    assert prod.weight == 15
    assert prod.flammability == 20


def test_product_stealability():
    '''Tests stealability method responses based on varying
    weight input values
    '''
    new_prod_one = Product('prod 1', weight=21)
    assert new_prod_one.stealability() == "Not so stealable..."

    new_prod_two = Product('prod 1', weight=20)
    assert new_prod_two.stealability() == "Kinda stealable."

    new_prod_three = Product('prod 1', weight=10)
    assert new_prod_three.stealability() == "Very stealable!"


def test_product_explode():
    '''Tests explode method responses based on varying
    flammability input values
    '''
    new_prod_one = Product('prod 1', flammability=0.4)
    assert new_prod_one.explode() == "...fizzle."

    new_prod_two = Product('prod 1', flammability=0.5)
    assert new_prod_two.explode() == "...boom!"

    new_prod_three = Product('prod 1', flammability=2.6)
    assert new_prod_three.explode() == "...BABOOM!!"


def test_generate_products_function():
    '''Tests generate_products function responses from acme_report module
    default response first, custom num_product second

    '''
    prod_list = generate_products()
    assert len(prod_list) == 30

    list_length = 10
    prod_list_2 = generate_products(num_products=list_length)
    assert len(prod_list_2) == list_length
