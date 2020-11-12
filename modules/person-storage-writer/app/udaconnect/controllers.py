from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource, Namespace, fields

from app.udaconnect.models import Person
from app.udaconnect.schemas import PersonSchema
from app.udaconnect.services import PersonService

api = Namespace("UdaConnect-Person", description="Write operations related to Persons in UdaConnect")  # noqa
person_model = api.model("Person Model", {
    "id": fields.String(description='id', required=True),
    "first_name": fields.String(description='first_name', required=True),
    "last_name": fields.String(description='last_name', required=True),
    "company_name": fields.String(description='company_name', required=True)
})


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    @api.param("payload", _in="body")
    @api.expect(person_model)
    @api.response(200, 'Person Resource successfully created.', person_model)
    def post(self) -> Person:
        """Creates a new Person Resource"""
        payload = request.get_json()
        new_person: Person = PersonService.create(payload)
        return new_person
