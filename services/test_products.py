from fastapi.testclient import TestClient
from products import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"What a": "page"}

def test_read_products():
    response = client.get("/products")
    assert response.status_code == 200
    json = response.json()
    assert(json['data'] != None)
    print(type(json['data']))
    assert isinstance(json['data'],list)