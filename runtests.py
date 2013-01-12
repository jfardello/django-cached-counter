#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath
import argparse
from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test.db',
            },
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'tests',
        ],
        ROOT_URLCONF='tests.urls',
        DEBUG=False,
        SITE_ID=1,
        CACHES={
            "default": {
                "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            },
        },
    )

from django.test.simple import DjangoTestSuiteRunner

def runtests(*args, **kwargs):
    dts = DjangoTestSuiteRunner(
            verbosity=kwargs.get('verbosity', 1),
            interactive=kwargs.get('interactive', False),
            failfast=kwargs.get('failfast')
    )
    failures = dts.run_tests(*args)
    sys.exit(failures)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--failfast', action='store_true', default=False, dest='failfast')
    parser.add_argument(
        '--interactive', action='store_true', default=False, dest='interactive')
    parser.add_argument('--verbosity', type=int, default=1, dest='verbosity')
    args = parser.parse_args()
    runtests(['tests'], verbosity=args.verbosity, interactive=args.interactive,
            failfast=args.failfast)
