from random import choice
import pytest
from HW_18_database.sql_user_table import SqliteUsersTable
from HW_18_database.sql_products_table import SqliteProductsTable


@pytest.fixture
def create_delete_user() -> dict:
    user_data = {
        "user_id": choice(range(3, 10000)),
        'name': 'Alex',
        'age': 20,
        'mail': 'Alex@mail.com',
    }

    SqliteUsersTable().create_user(**user_data)
    yield user_data
    SqliteUsersTable().delete_user_by_id(user_id=user_data['user_id'])


@pytest.fixture
def create_delete_product() -> dict:
    product_data = {
        "product_id": choice(range(3, 10000)),
        'model': 'Vaio',
        'brand': 'Sony',
        'warehouse': 'Lviv',
        'price': 800
    }

    SqliteProductsTable().create_product(**product_data)
    yield product_data
    SqliteProductsTable().delete_product_by_id(product_id=product_data['product_id'])
