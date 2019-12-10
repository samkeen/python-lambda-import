import json


from hello_world import app


def test_lambda_handler():

    ret = app.lambda_handler({}, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world, Goodbye"
