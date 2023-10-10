from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_convert_currency():
    response = client.get("/?source=USD&target=JPY&amount=$1,525")
    assert response.status_code == 200
    # python四捨五入 尾數遇偶則不進 170,496.525 -> 170,496.52
    assert response.json() == {"msg": "success", "amount": "$170,496.52"}

    # test source not in currencies
    response = client.get("/?source=EUR&target=JPY&amount=$1,525")
    assert response.status_code == 422

    # test target not in currencies
    response = client.get("/?source=USD&target=EUR&amount=$1,525")
    assert response.status_code == 422

    # test invalid amount
    response = client.get("/?source=USD&target=JPY&amount=$test")
    assert response.status_code == 400
