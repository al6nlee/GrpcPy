from generated.hello import hello_pb2_grpc, hello_pb2


class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message='Hello, %s!' % request.name)
