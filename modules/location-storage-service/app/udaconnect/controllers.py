from typing import List

from flask_accepts import responds
from flask_restx import Resource, Namespace, fields

from app.udaconnect.models import Location
from app.udaconnect.schemas import LocationSchema
from app.udaconnect.services import LocationService

api = Namespace("UdaConnect-Location", description="Connections via geolocation.")  # noqa
resource_fields = api.model("Location Model", {
    "person_id": fields.Integer(description='person_id', required=True),
    "creation_time": fields.String(description='creation_time', required=True),
    "latitude": fields.String(description='latitude', required=True),
    "longitude": fields.String(description='longitude', required=True)
})


@api.route("/location/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location


@api.route("/locations")
class LocationsResource(Resource):

    @responds(schema=LocationSchema, many=True)
    def get(self) -> List[Location]:
        locations: List[Location] = LocationService.retrieve_all()
        return locations
