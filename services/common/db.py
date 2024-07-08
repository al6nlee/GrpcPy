import mysql.connector


class MySQLConnectionPool:
    def __init__(self, pool_name="grpc-pool", pool_size=10):
        self.pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            host="172.26.22.201",
            user="root",
            password="12345678",
            database="grpc"
        )

    def get_connection(self):
        return self.pool.get_connection()


db_pool = MySQLConnectionPool()
