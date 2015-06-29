import os
from setuptools import setup, find_packages

setup(name='morepath_batching',
      version='0.1.dev0',
      description="Morepath Batching Demo",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'morepath',
        'more.jinja2',
        'fake-factory'
        ],
      entry_points= {
        'console_scripts': [
            'morepath_batching = morepath_batching.main:main',
            ]
        },
      )
