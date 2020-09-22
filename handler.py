from flask import Flask, request, jsonify
import requests
import json

from adapter import Adapter

def handle(event, context):
    ploads = {'things':2,'total':25}
    r = requests.get('https://httpbin.org/get',params=ploads)
    body = event["body"]
    y = json.loads(body)
    print(y)
    data = y
    if data == '':
        data = {}
    adapter = Adapter(data)
    return {
      "body": json.dumps(adapter.result),
      "statusCode": 200,
    }
