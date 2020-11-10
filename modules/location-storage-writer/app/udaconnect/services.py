import logging
from typing import Dict

from geoalchemy2 import Geometry
from geoalchemy2.functions import ST_Point

from app import producer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

TOPIC_NAME = 'locations'


class Location:
    def __init__(self, person_id, creation_time, coordinate):
        self.person_id = person_id
        self.creation_time = creation_time
        self.coordinate = coordinate


class LocationService:

    @staticmethod
    def publishToKafka(location: Dict) -> Location:
        # validation_results: Dict = LocationSchema().validate(location)
        # if validation_results:
        #     logger.warning(f"Unexpected data format in payload: {validation_results}")
        #     raise Exception(f"Invalid payload: {validation_results}")
        coordinate:Geometry = ST_Point(location["latitude"], location["longitude"])
        new_location = Location(location["person_id"], location["creation_time"], coordinate )
        # new_location.person_id = location["person_id"]
        # new_location.creation_time = location["creation_time"]

        producer.send(TOPIC_NAME, b'new_location.person_id')
        producer.flush()

        return new_location
