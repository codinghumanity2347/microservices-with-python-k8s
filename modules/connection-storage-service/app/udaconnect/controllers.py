from datetime import datetime
from typing import Optional

from flask import request
from flask_accepts import responds
from flask_restx import Resource, Namespace, fields

from app.udaconnect.schemas import ConnectionSchema
from app.udaconnect.services import ConnectionService

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect-Connections", description="Connections via geolocation.")  # noqa
connection_model = api.model("Connection Model", {
    "location": fields.Nested(api.model("Location Model", {
        "id": fields.Integer(description='id', required=True),
        "person_id": fields.Integer(description='person_id', required=True),
        "creation_time": fields.String(description='creation_time', required=True),
        "latitude": fields.String(description='latitude', required=True),
        "longitude": fields.String(description='longitude', required=True)
    })), "person": fields.Nested(api.model("Person Model", {
        "id": fields.String(description='id', required=True),
        "first_name": fields.String(description='first_name', required=True),
        "last_name": fields.String(description='last_name', required=True),
        "company_name": fields.String(description='company_name', required=True)
    }))
})


@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    @api.response(200, 'Success', [connection_model])
    def get(self, person_id) -> ConnectionSchema:
        """Returns a List of near by connections for a user"""
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return results
