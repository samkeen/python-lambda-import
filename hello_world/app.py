import json



print(f'__file__={__file__} | __name__={__name__} | __package__={str(__package__)}')

from .lib.foo import goodbye

def lambda_handler(event, context):
    resp = "hello world, " + goodbye()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": resp,
        }),
    }
