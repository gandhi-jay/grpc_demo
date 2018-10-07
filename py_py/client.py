import grpc

# import generated classes
import calc_pb2
import calc_pb2_grpc

# open a GRPC channel
# make sure about the port and address.
channel = grpc.insecure_channel('localhost:8081')

# create a stub
stub = calc_pb2_grpc.CalculatorStub(channel)

number = calc_pb2.Number(value=16)

response = stub.SquareRoot(number)

print(type(response))
print(response)