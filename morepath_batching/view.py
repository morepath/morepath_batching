from .model import PersonCollection, Person
from .app import App


@App.template_directory()
def get_template_directory():
    return 'templates'


@App.html(model=PersonCollection, template='person_collection.jinja2')
def person_collection_default(self, request):
    return {
        'persons': self.query(),
        'previous_link': request.link(self.previous()),
        'next_link': request.link(self.next()),
    }


@App.html(model=Person, template='person.jinja2')
def person_default(self, request):
    return {
        'id': self.id,
        'name': self.name,
        'address': self.address,
        'email': self.email
    }
