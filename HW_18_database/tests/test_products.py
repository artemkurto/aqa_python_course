from HW_18_database.sql_products_table import SqliteProductsTable
from assertpy import assert_that
from random import choice
import pytest
import sqlite3


def test_get_all_products():
    products = SqliteProductsTable().get_all_products()
    assert_that(len(products), 'Products > 0').is_not_zero()


def test_create_product():
    products_len = len(SqliteProductsTable().get_all_products())
    SqliteProductsTable().create_product()
    assert len(SqliteProductsTable().get_all_products()) == products_len + 1


def test_get_price_by_id():
    product_id = 8786
    price = SqliteProductsTable().get_price_by_id(product_id)[0][0]
    assert isinstance(price, (int, float))


def test_update_price():
    product_id = 8786
    new_price = 800
    old_price = SqliteProductsTable().get_price_by_id(product_id)[0][0]
    SqliteProductsTable().update_price_by_id(product_id, new_price)
    assert SqliteProductsTable().get_price_by_id(product_id)[0][0] == new_price
    SqliteProductsTable().update_price_by_id(product_id, old_price)


def test_delete_product():
    product_data = {
        "product_id": choice(range(3, 10000)),
        'model': 'macbook',
        'brand': 'Apple',
        'warehouse': 'Dnipro',
        'price': 1800
    }
    products_len = len(SqliteProductsTable().get_all_products())
    SqliteProductsTable().create_product(**product_data)
    SqliteProductsTable().delete_product_by_id(product_id=product_data['product_id'])
    assert len(SqliteProductsTable().get_all_products()) == products_len


def test_get_product_by_wrong_id():
    product_id = 9999999
    assert SqliteProductsTable().get_product_by_id(product_id) == []


def test_update_price_negative():
    product_id = 8786
    new_price = '800$'
    with pytest.raises(sqlite3.OperationalError):
        SqliteProductsTable().update_price_by_id(product_id, new_price)
    # try:
    #     SqliteProductsTable().update_price_by_id(product_id, new_price)
    # except sqlite3.OperationalError as e:
    #     print(f"Виникла помилка: {e}")
