from currency.models import ContactUs, Rate

from django.conf import settings


def test_get_rates(api_client):
    response = api_client.get('/api/rates/')
    assert response.status_code == 200
    assert response.json()


def test_invalid_post_rates(api_client):
    response = api_client.post('/api/rates/')
    assert response.status_code == 400
    assert response.json() == {
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'source': ['This field is required.'],
    }


def test_valid_post_rates(api_client, load_fixtures):
    initial_count = Rate.objects.count()
    payload = {
        "sale": 30,
        "buy": 30,
        "source": 17
    }
    response = api_client.post('/api/rates/', data=payload)
    assert response.status_code == 201
    assert Rate.objects.count() == initial_count + 1


def test_get_contactus(api_client):
    response = api_client.get('/api/contactus/')
    assert response.status_code == 200
    assert response.json()


def test_valid_post_contactus(api_client, mailoutbox):
    initial_count = ContactUs.objects.count()
    payload = {
        "name": 'name',
        "reply_to": 'reply_to@email.com',
        "subject": 'subject',
        "body": 'body'
    }
    response = api_client.post('/api/contactus/', data=payload)
    assert response.status_code == 201
    assert ContactUs.objects.count() == initial_count + 1
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL


def test_get_source(api_client, load_fixtures):
    response = api_client.get('/api/sources/')
    assert response.status_code == 200
    assert response.json()


def test_post_source(api_client):
    response = api_client.post('/api/sources/')
    assert response.status_code == 405


def test_put_source(api_client):
    response = api_client.put('/api/sources/')
    assert response.status_code == 405


def test_delete_source(api_client):
    response = api_client.delete('/api/sources/')
    assert response.status_code == 405
