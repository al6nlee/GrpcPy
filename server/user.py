from concurrent import futures
import grpc
from generated.user import user_pb2_grpc
from services.common.db import db_pool
from services.user.service_user import UserService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(db_pool), server)
    server.add_insecure_port('[::]:7878')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
