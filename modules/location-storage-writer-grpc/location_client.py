from __future__ import print_function

import logging

from google.protobuf.timestamp_pb2 import Timestamp

import grpc
import location_pb2
import location_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:30005') as channel:
        stub = location_pb2_grpc.LocationServiceStub(channel)

        timestamp = Timestamp()
        response = stub.updateLocation(
            location_pb2.Location(personId=111, latitude=10, longitude=30, createdTime=timestamp.GetCurrentTime()))
        print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
