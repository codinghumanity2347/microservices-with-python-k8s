from typing import List

from flask_accepts import responds
from flask_restx import Resource, Namespace, fields

from app.udaconnect.models import Person
from app.udaconnect.schemas import PersonSchema
from app.udaconnect.services import PersonService

api = Namespace("UdaConnect-Person", description="Read operations related to Persons in UdaConnect.")  # noqa
person_model = api.model("Person Model", {
    "id": fields.String(description='id', required=True),
    "first_name": fields.String(description='first_name', required=True),
    "last_name": fields.String(description='last_name', required=True),
    "company_name": fields.String(description='company_name', required=True)
})


@api.route("/persons")
class PersonsResource(Resource):
    @responds(schema=PersonSchema, many=True)
    @api.response(200, 'Success', [person_model])
    def get(self) -> List[Person]:
        """Returns List of all Persons."""
        return PersonService.retrieve_all()


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    @api.response(404, 'Person not found')
    @api.response(200, 'Success', person_model)
    def get(self, person_id) -> Person:
        """Returns Details of Person"""
        person: Person = PersonService.retrieve(person_id)
        return person
