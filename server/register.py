from generated.hello import hello_pb2_grpc
from generated.user import user_pb2_grpc
from server.common.db import db_pool
from server.services.hello.service_hello import Greeter
from server.services.user.service_user import UserService


def register(server):
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(db_pool), server)
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
