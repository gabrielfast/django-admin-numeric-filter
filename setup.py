#!/usr/bin/env python
from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name='django-admin-numeric-filter',
    short_description='Numeric filters for Django admin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.2',
    packages=[
        'admin_numeric_filter',
    ],
    include_package_data=True,
    install_requires=('django', ),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
    ],
    keywords="django admin numeric filter"
)
