import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.udaconnect.models import Person

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


class PersonService:
    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()
