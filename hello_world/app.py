import json

from .foo import goodbye


def lambda_handler(event, context):
    resp = "hello world, " + goodbye()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": resp,
        }),
    }
