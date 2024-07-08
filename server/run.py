from concurrent import futures
import grpc

from server.config import SERVER_PORT
from server.register import register


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    register(server)
    server.add_insecure_port(f'[::]:{SERVER_PORT}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()
