from http import HTTPStatus


def test_read_root_deve_retornar_status_code_OK(client):
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert


def test_read_root_deve_retornar_mensagem_hello_world(client):
    # act
    response = client.get('/')
    # assert
    assert response.json() == {'message': 'Hello, world!'}


def test_exercicio_dois_deve_retornar_status_code_OK(client):
    response = client.get('/olamundo')  # act
    assert response.status_code == HTTPStatus.OK  # assert


def test_exercicio_dois_deve_retornar_html_com_h1_hello_world(client):
    # act
    response = client.get('/olamundo')

    # assert
    assert '<h1>Hello, World!</h1>' in response.text


def test_create_user_deve_retornar_status_code_CREATED(client):
    response = client.post(
        '/users/',
        json={
            'username': 'sophie',
            'email': 'sophie@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED


def test_create_user_deve_retornar_user(client):
    # act
    response = client.post(
        '/users/',
        json={
            'username': 'ana',
            'email': 'ana@example.com',
            'password': 'secret',
        },
    )
    # assert
    assert response.json() == {
        'id': 2,
        'username': 'ana',
        'email': 'ana@example.com',
    }


def test_get_users_deve_retornar_status_code_OK(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK


def test_get_users_deve_retornar_lista_de_users_criados(client):
    response = client.get('/users/')

    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'sophie',
                'email': 'sophie@example.com',
            },
            {
                'id': 2,
                'username': 'ana',
                'email': 'ana@example.com',
            }
        ]
    }


def test_update_user_deve_retornar_status_code_OK(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'sophie atualizada',
            'email': 'sophie.update@example.com',
            'password': 'secret',
            'id': 1,
        },
    )
    assert response.status_code == HTTPStatus.OK


def test_update_user_deve_retornar_user_atualizado(client):
    # act
    response = client.put(
        '/users/1',
        json={
            'username': 'sophie atualizada',
            'email': 'sophie.update@example.com',
            'password': 'secret',
            'id': 1,
        },
    )
    # assert
    assert response.json() == {
        'id': 1,
        'username': 'sophie atualizada',
        'email': 'sophie.update@example.com',
    }


def test_update_user_com_id_inexistente_deve_retornar_NOT_FOUND(client):
    # act
    response = client.put(
        '/users/5',
        json={
            'username': 'user inexistente',
            'email': 'user.inexistente@example.com',
            'password': 'secret',
            'id': 5,
        },
    )
    # assert
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_user_by_id_deve_retornar_status_code_OK(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK


def test_get_user_by_id_deve_retornar_user(client):
    response = client.get('/users/1')
    assert response.json() == {
        'id': 1,
        'username': 'sophie atualizada',
        'email': 'sophie.update@example.com',
    }


def test_delete_user_deve_retornar_OK_e_mensagem_user_deleted(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_com_id_inexistente_deve_retornar_NOT_FOUND(client):
    response = client.delete('/users/5')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_user_by_id_inexistente_deve_retornar_NOT_FOUND(client):
    response = client.get('/users/5')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'USER NOT FOUND'}
