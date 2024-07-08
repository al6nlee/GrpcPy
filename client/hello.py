import grpc
from generated.hello import hello_pb2, hello_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:7878') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='world'))
        print('Greeter client received: ' + response.message)


if __name__ == '__main__':
    run()
