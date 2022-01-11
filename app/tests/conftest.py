from django.core.management import call_command

import pytest

from rest_framework.test import APIClient


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to datebase for all tests
    """


@pytest.fixture(scope="function")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = (
            'source.json',
            'rates.json',
        )
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')


@pytest.fixture(scope='function')
def api_client(django_user_model):
    client = APIClient()
    yield client
