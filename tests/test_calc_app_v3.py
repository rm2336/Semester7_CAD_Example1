from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


# calling root
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    # exact JSON
    assert response.json() == {"message": "Hello, Microservice!"}


# test multiplication
def test_calculator():
    #
    # validate 2*3 = 6
    response = client.post("/operations", json={"num1": 2, "opt": "*",
                                                "num2": 3})
    assert response.status_code == 200
    assert response.json() == {'data': {'num1': 2, 'num2': 3, 'opt': '*',
                                        'result': 6.0},
                               'message': 'Success'}


# check if SwaggerUI is up and running (for FastAPI)
def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200
