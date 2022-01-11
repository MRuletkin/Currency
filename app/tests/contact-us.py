from currency.models import ContactUs


def test_get(client):
    response = client.get('/currency/contactus/create/')
    assert response.status_code == 200


def test_post_empty_form(client):
    response = client.post('/currency/contactus/create/')
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'name': ['This field is required.'],
        'reply_to': ['This field is required.'],
        'subject': ['This field is required.'],
        'body': ['This field is required.'],
    }


def test_post_invalid_email(client):
    initial_count = ContactUs.objects.count()
    payload = {
        'name': 'Name',
        'reply_to': 'INVALID-EMAIL',
        'subject': 'subject',
        'body': 'body',
    }
    response = client.post('/currency/contactus/create/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'reply_to': ['Enter a valid email address.']}
    assert ContactUs.objects.count() == initial_count


def test_post_valid(client, mailoutbox, settings):
    initial_count = ContactUs.objects.count()
    payload = {
        'name': 'Name',
        'reply_to': 'example@mail.com',
        'subject': 'subject',
        'body': 'body',
    }
    response = client.post('/currency/contactus/create/', data=payload)
    assert response.status_code == 302
    assert response['location'] == '/'
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL

    assert ContactUs.objects.count() == initial_count + 1
