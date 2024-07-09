import os

from server.global_conf.global_conf import global_conf


def load_config(key, default=None):
    # 先从环境变量中获取配置
    value = os.getenv(key)
    if value is not None:
        return value
    # 如果配置文件中也没有该配置，返回默认值
    return global_conf.get(key, default)


SERVER_MAX_WORKERS = load_config("SERVER_MAX_WORKERS", 10)
SERVER_PORT = load_config("PORT", 7878)

# MYSQL global_conf
MYSQL_HOST = load_config("MYSQL_HOST", "172.26.22.201")
MYSQL_USER = load_config("MYSQL_USER", "root")
MYSQL_PASSWORD = load_config("MYSQL_PASSWORD", "12345678")
MYSQL_DB = load_config("MYSQL_DB", "grpc")
MYSQL_PORT = load_config("MYSQL_PORT", 3306)
MYSQL_POOL_SIZE = load_config("MYSQL_POOL_SIZE", 5)
MYSQL_POOL_NAME = load_config("MYSQL_POOL_NAME", "grpc-pool")
