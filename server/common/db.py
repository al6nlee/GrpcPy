import mysql.connector

from server.config import (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_POOL_SIZE,
                           MYSQL_POOL_NAME)


class MySQLConnectionPool:
    def __init__(self, pool_name=MYSQL_POOL_NAME, pool_size=MYSQL_POOL_SIZE):
        self.pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )

    def get_connection(self):
        return self.pool.get_connection()


db_pool = MySQLConnectionPool()
