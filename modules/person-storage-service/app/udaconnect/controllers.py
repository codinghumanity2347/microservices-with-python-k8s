from typing import List

from flask_accepts import responds
from flask_restx import Resource, Namespace

from app.udaconnect.models import Person
from app.udaconnect.schemas import PersonSchema
from app.udaconnect.services import PersonService

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


@api.route("/persons")
class PersonsResource(Resource):
    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        return PersonService.retrieve_all()


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person
