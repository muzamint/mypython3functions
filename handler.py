import requests

def handle(event, context):
    ploads = {'things':2,'total':25}
    r = requests.get('https://httpbin.org/get',params=ploads)
    return {
        "body": r.text,
        "statusCode": 200,
    }