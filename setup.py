# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages


setup(
    name='morepath_batching',
    version='0.2.dev0',
    description=(
        'A demo app for Morepath with record batching'
    ),
    long_description=(
        io.open('README.rst', encoding='utf-8').read() + '\n\n' +
        io.open('CHANGES.rst', encoding='utf-8').read()),
    author='Morepath developers',
    author_email='morepath@googlegroups.com',
    license="BSD",
    url="https://github.com/morepath/morepath_batching",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords='morepath demo',
    install_requires=[
        'morepath>=0.14',
        'more.jinja2',
        'Faker',
    ],
    extras_require=dict(
        test=[
            'pytest',
            'pytest-cov',
            'webtest',
        ],
    ),
    entry_points={
        'console_scripts': [
            'morepath_batching = morepath_batching.__main__:run',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
