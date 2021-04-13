import pytest

pytestmark = pytest.mark.django_db


def test_app():
    assert True


def test_home(client):
    response = client.get('')
    assert response.status_code == 200
    assert 'home.html' in response.template_name
