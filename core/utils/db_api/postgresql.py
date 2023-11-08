from typing import Uninon

import asyncpg
from asuncpg.pool import Pool
from asuncpg.connection import Connection

import settings


class Database:
    def __init__(self):
        self.pool: Uninon[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user = 'postgres',
            password = 'postgres',
            host = 'localhost',
            database = 'postgres',
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False,
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    #Функция создания таблицы юзеров
    async def create_users_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NOT NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO Users(full_name, username, telegram_id) VALUES ($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)
    async def select_all_users(self):
        sql = " SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = " SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = " SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_username(self, username, telegram_id):
        sql = "UPDATE Users SET username = $1 WHERE telegram_id = $2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)


    #Функции для работы с корзиной
    async def get_products(self, category_id):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM products WHERE category_id=(?)""", [category_id]).fetchall()

    async def get_user_product(self, product_id):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM products WHERE product_id=(?)""", [product_id]).fetchall()

    async def get_cart(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM cart WHERE user_id=(?)""", [user_id]).fetchall()

    async def add_to_cart(self, user_id, product_id):
        with self.connect:
            return self.cursor.execute("""INSERT INTO cart (user_id, product_id, count) VALUES (?, ?, ?)""",
                                       [user_id, product_id, 1])

    async def empty_cart(self, user_id):
        with self.connect:
            return self.cursor.execute("""DELETE FROM cart WHERE user_id=(?)""", [user_id])

    async def get_categories(self):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM categories""").fetchall()

    async def get_count_in_cart(self, user_id, product_id):
        with self.connect:
            return self.cursor.execute("""SELECT count FROM cart WHERE user_id=(?) AND product_id=(?)""",
                                       [user_id, product_id]).fetchall()

    async def get_count_in_stock(self, product_id):
        with self.connect:
            return self.cursor.execute("""SELECT count FROM products WHERE product_id=(?)""",
                                       [product_id]).fetchall()

    async def remove_one_item(self, product_id, user_id):
        with self.connect:
            return self.cursor.execute("""DELETE FROM cart WHERE product_id=(?) AND user_id=(?)""",
                                       [product_id, user_id])

    async def change_count(self, count, product_id, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE cart SET count=(?) WHERE product_id=(?) AND user_id=(?)""",
                                       [count, product_id, user_id])