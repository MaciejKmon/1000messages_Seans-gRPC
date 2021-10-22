import os
import pingping_pb2
import pingping_pb2_grpc
import time
import grpc

def run():
    counter = 0
    pid = os.getpid()
