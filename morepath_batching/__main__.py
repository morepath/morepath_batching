import morepath
from .app import App


def run():
    morepath.run(App())


if __name__ == '__main__':  # pragma: no cover
    run()
