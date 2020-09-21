import json

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event["body"])
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps(body["key2"])
    }
