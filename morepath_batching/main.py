import morepath
from more.jinja2 import Jinja2App


class App(Jinja2App):
    pass


def main():
    morepath.autosetup()
    morepath.run(App())
