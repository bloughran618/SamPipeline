import json


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello to the world",
            # "location": ip.text.replace("\n", "")
        }),
    }
