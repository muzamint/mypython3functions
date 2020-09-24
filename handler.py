from flask import Flask, request, jsonify
import requests
import json
import datetime
import sys

from adapter import Adapter

def handle(event, context):
    body = event['body']
    if body == None:
      print("NONE")
    data = json.loads(event['body'])
    print(data)
    adapter = Adapter(data)
    return {
      "body": json.dumps(adapter.result, indent=2),
      "statusCode": 200,
      "headers": {
      "Content-Type": "application/json",
      }
    }
