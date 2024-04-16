from random import choice
from HW_18_database.db_base.base_sql_table import execute_sql_query


class SqliteProductsTable:

    def __init__(self):
        self.db_name = 'test_db.db'
        self.table_name = 'Products'

    @execute_sql_query
    def get_all_products(self):
        return f'select * from {self.table_name}'

    @execute_sql_query
    def get_product_by_id(self, product_id):
        return f'select * from {self.table_name} where id = {product_id}'

    @execute_sql_query
    def create_product(self, product_id=None, model='legion5 ', brand='lenovo', warehouse='lviv', price=400.50):
        product_id = product_id or choice(range(3, 10000))
        return f'insert into {self.table_name} values ({product_id}, "{model}", "{brand}", "{warehouse}", {price})'

    @execute_sql_query
    def get_price_by_id(self, product_id):
        return f"select price from {self.table_name} where id={product_id}"

    @execute_sql_query
    def update_price_by_id(self, product_id, new_price):
        return f"UPDATE Products SET price={new_price} where id={product_id}"

    @execute_sql_query
    def delete_product_by_id(self, product_id):
        return f'delete from {self.table_name} where id = {product_id}'

    @execute_sql_query
    def create_table(self):
        return """
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    model TEXT,
    brand TEXT,
    warehouse TEXT,
    price NUMERIC 
);
"""



