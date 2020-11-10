from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource, Namespace, fields

from app.udaconnect.models import Person
from app.udaconnect.schemas import PersonSchema
from app.udaconnect.services import PersonService

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa
resource_fields = api.model("Person Model", {
    "first_name": fields.String(description='first_name', required=True),
    "last_name": fields.String(description='last_name', required=True),
    "company_name": fields.String(description='company_name', required=True)
})


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    @api.param("payload", _in="body")
    @api.expect(resource_fields)
    def post(self) -> Person:
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person
