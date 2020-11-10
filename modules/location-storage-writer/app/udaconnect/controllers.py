from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource, Namespace, fields

from app.udaconnect.services import LocationService

api = Namespace("UdaConnect-Location", description="Connections via geolocation.")  # noqa
resource_fields = api.model("Location Model", {
    "person_id": fields.Integer(description='person_id', required=True),
    "creation_time": fields.String(description='creation_time', required=True),
    "latitude": fields.String(description='latitude', required=True),
    "longitude": fields.String(description='longitude', required=True)
})


@api.route("/location")
class LocationResource(Resource):
    @accepts(model_name="Location Model")
    @responds(model_name="Location Model")
    @api.param("payload", _in="body")
    @api.expect(resource_fields)
    def post(self):
        request.get_json()
        LocationService.publishToKafka(request.get_json())
