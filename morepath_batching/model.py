from faker import Faker


BATCH_SIZE = 10


class Person(object):
    def __init__(self, id, name, address, email):
        self.id = id
        self.name = name
        self.address = address
        self.email = email


class PersonCollection(object):
    def __init__(self, persons, start):
        self.persons = persons
        if start < 0 or start >= len(persons):
            start = 0
        self.start = start

    def query(self):
        return self.persons[self.start:self.start + BATCH_SIZE]

    def previous(self):
        if self.start == 0:
            return None
        start = self.start - BATCH_SIZE
        if start < 0:
            start = 0
        return PersonCollection(self.persons, start)

    def next(self):
        start = self.start + BATCH_SIZE
        if start >= len(self.persons):
            return None
        return PersonCollection(self.persons, self.start + BATCH_SIZE)


fake = Faker()


def generate_random_person(id):
    return Person(id, fake.name(), fake.address(), fake.email())


def generate_random_persons(amount):
    return [generate_random_person(id) for id in range(amount)]


person_db = generate_random_persons(56)
