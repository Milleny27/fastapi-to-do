from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_OK_e_ola_mundo():
    # arrange
    client = TestClient(app)

    # act
    response = client.get('/')

    # assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, world!'}


def test_exercicio_dois_deve_retornar_OK_e_ola_mundo_no_htlm():
    # arrange
    client = TestClient(app)

    # act
    response = client.get('/olamundo')

    # assert
    assert response.status_code == HTTPStatus.OK
    assert '<h1>Hello, World!</h1>' in response.text
