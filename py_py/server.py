import grpc
from concurrent import futures
import time

# Import generated Classes from this command
# python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calc.proto
import calc_pb2
import calc_pb2_grpc

import calculator

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calc_pb2_grpc.CalculatorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def SquareRoot(self, request, context):
        print("[DEBUG] %s" % request)
        resp = calc_pb2.Number()
        resp.value = calculator.square_root(request.value)
        return resp

# Creating server of GRPC.
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
calc_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

# Listen on port 8081
print("Starting Server on 8081")
server.add_insecure_port('[::]:8081')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)