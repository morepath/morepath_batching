from webtest import TestApp as Client
from .. import App
from ..__main__ import run
from ..model import person_db


def test_random_access_record():
    c = Client(App())
    assert person_db[14].name in c.get('/14').html.p.text
    c.get('/101', status=404)


def test_pagination():
    c = Client(App())

    records = []
    url = '/'
    records_in_page = []

    for page_number in range(10):  # go through at most 10 pages
        r = c.get(url)

        if page_number == 0:
            # The first page does not have a "previous" link
            assert r.html.findAll('a', text='Previous') == []
        else:
            prev, = [a['href'] for a in r.html.findAll('a', text='Previous')]
            assert c.get(prev).html.select('table a') == records_in_page

        # Get the link to the next page or None if at the end
        url, = [a['href'] for a in r.html.findAll('a', text='Next')] or [None]

        records_in_page = r.html.select('table a')
        assert len(records_in_page) <= 10
        if url is not None:
            assert len(records_in_page) == 10
        records.extend(records_in_page)

        if url is None:
            break

    # We got all 56 records
    assert len(records) == 56

    # and all 6 pages (starting from 0)
    assert page_number == 5

    for rec in records:
        assert rec.text in c.get(rec['href']).html.p.text


def test_non_aligned_page():
    c = Client(App())

    r = c.get('/?start=5')
    assert (
        [a.text for a in r.html.select('table a')] ==
        [p.name for p in person_db[5:15]]
    )
    prev_url, = [a['href'] for a in r.html.findAll('a', text='Previous')]
    assert (
        [a.text for a in c.get(prev_url).html.select('table a')] ==
        [p.name for p in person_db[:10]]
    )


def test_out_of_bounds_page():
    c = Client(App())

    r = c.get('/?start=-4')
    assert (
        [a.text for a in r.html.select('table a')] ==
        [p.name for p in person_db[:10]]
    )


def test_run(monkeypatch):
    import morepath
    instances = []
    monkeypatch.setattr(morepath, 'run', lambda app: instances.append(app))

    run()

    app, = instances
    assert isinstance(app, App)
