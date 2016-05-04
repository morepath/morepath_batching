from .app import App
from .model import PersonCollection, Person, person_db


@App.path(model=PersonCollection, path='/')
def get_person_collection(start=0):
    return PersonCollection(person_db, start)


@App.path(model=Person, path='{id}',
          converters={'id': int})
def get_person(id):
    try:
        return person_db[id]
    except IndexError:
        return None
