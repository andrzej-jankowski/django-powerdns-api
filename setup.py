# -*- encoding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages


assert sys.version_info >= (2, 7), "Python 2.7+ required."


current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, current_dir + os.sep + 'src')


setup(
    name='django-powerdns-api',
    version='0.1.0',
    license='Apache Software License v2.0',
    author='Andrzej Jankowski',
    url='',
    author_email='andrew.jankowski@gmail.com',
    description='API for PowerDNS administration module.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django-powerdns-dnssec>=0.10.0',
        'djangorestframework==3.0.4',
        'django-filter==0.9.2',
    ],
    classifiers=[
        'Development Status :: 0.1.0 - Beta',
        'Framework :: Django',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License v2.0',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
