import json

import os, sys
this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_dir)

from foo import goodbye


def lambda_handler(event, context):
    resp = "hello world, " + goodbye()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": resp,
        }),
    }
