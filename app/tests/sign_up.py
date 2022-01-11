from accounts.models import User


def test_empty_post(client):
    response = client.post('/accounts/signup/')
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['This field is required.'],
        'password': ['This field is required.'],
        'password_confirm': ['This field is required.']
    }


def test_invalid_email_post(client):
    initial_count = User.objects.count()
    payload = {
        'email': 'email',
        'password': 'password',
        'password_confirm': 'password',
    }
    response = client.post('/accounts/signup/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email': ['Enter a valid email address.']}
    assert User.objects.count() == initial_count


def test_invalid_password_post(client):
    initial_count = User.objects.count()
    payload = {
        'email': 'email@dom.com',
        'password': 'passwords',
        'password_confirm': 'password',
    }
    response = client.post('/accounts/signup/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'__all__': ["Passwords don't match."]}
    assert User.objects.count() == initial_count


def test_valid_post(client):
    initial_count = User.objects.count()
    payload = {
        'email': 'email@dom.com',
        'password': 'password',
        'password_confirm': 'password',
    }
    response = client.post('/accounts/signup/', data=payload)
    assert response.status_code == 302
    assert response['location'] == '/'
    assert User.objects.count() == initial_count + 1
