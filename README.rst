Morepath Batching Demo
======================

Introduction
------------

This is a demo app for Morepath_ that illustrates *batching*, i.e.,
presenting a large data set by partitioning it in smaller batches.  It
also showcases how to use Jinja2_ templates in a Morepath project.

More information on this app is available on `Martjin Faassen' blog`_.


Getting started
---------------

To get started with this demo right away, you can install it and run it in
a newly created `virtual environment`_::

  $ virtualenv env
  $ ./env/bin/pip install morepath_batching
  $ ./env/bin/morepath_batching

You can now access the app at http://localhost:5000.


Installation from sources
-------------------------

You can grab the sources from GitHub_ and set them up in a fresh `virtual environment`_::

  $ git clone https://github.com/morepath/morepath_batching.git
  $ cd morepath_batching
  $ virtualenv env
  $ ./env/bin/pip install -e '.[test]'

You'll then be able to start the app::

  $ ./env/bin/morepath_batching

And to run the test suite::

  $ ./env/bin/py.test -v


.. _Morepath: http://morepath.readthedocs.io/

.. _Jinja2: http://jinja.pocoo.org
  
.. _GitHub: https://github.com/morepath/morepath_batching

.. _virtual environment: http://www.virtualenv.org/

.. _Martjin Faassen' blog: http://blog.startifact.com/posts/morepath-batching-example.html
