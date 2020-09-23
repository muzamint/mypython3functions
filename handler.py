from flask import Flask, request, jsonify
import requests
import json
import datetime
import sys

from adapter import Adapter

def handle(event, context):
    ploads = {'things':2,'total':25}
  #  r = requests.get('https://httpbin.org/get',params=ploads)
    print(sys.version)
    print(dir(context))
    print(event)
    x = datetime.datetime.now()
    print("ming-now")
    print(x)
    body = event["body"]
    body = "{\"id\": 0, \"data\": {\"base\": \"ETH\", \"quote\": \"USD\"}}"
    data = json.loads(body)   
    print(data)
    adapter = Adapter(data)
    return {
      "body": json.dumps(adapter.result, indent=2),
      "statusCode": 200,
      "headers": {
      "Content-Type": "application/json",
      },
    }
