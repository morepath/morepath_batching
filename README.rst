Morepath Batching Demo
======================

Show how to create a server web application with Morepath that uses
batching and Jinja2 templates.

Installation
------------

You can use pip in a virtual env::

  $ virtualenv ve
  $ ve/bin/pip install -e .

Then to run the web server::

  $ ve/bin/morepath_batching

You can now access the application through http://localhost:5000

Buildout
--------

Instead of pip in a virtualenv you can also use buildout::

  $ python bootstrap.py
  $ bin/buildout
  $ bin/morepath_batching
