import grpc
from generated.user import user_pb2
from generated.user import user_pb2_grpc


class UserService(user_pb2_grpc.UserServiceServicer):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    def CreateUser(self, request, context):
        conn = self.db_pool.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (request.name, request.email)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return user_pb2.CreateUserResponse(message="User created successfully")

    def GetUser(self, request, context):
        conn = self.db_pool.get_connection()
        cursor = conn.cursor()
        query = "SELECT id, name, email FROM users WHERE id = %s"
        cursor.execute(query, (request.id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return user_pb2.GetUserResponse(id=result[0], name=result[1], email=result[2])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.GetUserResponse()

    def UpdateUser(self, request, context):
        conn = self.db_pool.get_connection()
        cursor = conn.cursor()
        query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        values = (request.name, request.email, request.id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return user_pb2.UpdateUserResponse(message="User updated successfully")

    def DeleteUser(self, request, context):
        conn = self.db_pool.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (request.id,))
        conn.commit()
        cursor.close()
        conn.close()
        return user_pb2.DeleteUserResponse(message="User deleted successfully")
