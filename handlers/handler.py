import numpy

def handle(event, context):
    return {
        "body": {
            "numpy": {
              "version": numpy.__version__,
        }},
        "statusCode": 200,
    }