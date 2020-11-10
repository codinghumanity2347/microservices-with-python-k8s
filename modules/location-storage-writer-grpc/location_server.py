import os

import location_pb2_grpc
import location_pb2
from concurrent import futures
import logging
import grpc
from kafka import KafkaProducer

TOPIC_NAME = 'locations'
KAFKA_SERVER = os.environ["KAFKA_ADD"] #'localhost:9092'
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


class LocationServiceServicer(location_pb2_grpc.LocationServiceServicer):

    def updateLocation(self, request, context):
        location_message = location_pb2.Location(personId=request.personId, latitude=request.latitude,
                                                 longitude=request.longitude)

        producer.send(TOPIC_NAME, request.SerializeToString())
        producer.flush()
        return location_pb2.Status(currentState="Received")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(
        LocationServiceServicer(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
