from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, world!'}


@app.get('/olamundo', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def exercicio_dois():
    return """
        <html>
            <head>
                <title>Exercício Aula 02</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
            </body>
        </html>
        """
