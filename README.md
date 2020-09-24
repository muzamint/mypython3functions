# deploy
## you need a scaleway account first, serverless is free in beta
```
serverless deploy
```

# build package
if you import package need to compile with c/c++, such as numpy...
```
docker run --rm -v $(pwd):/home/app/function --workdir /home/app/function rg.fr-par.scw.cloud/scwfunctionsruntimes/python-dep3:v4.0.0 pip install numpy --target ./package
```
for python3

# debug locally
```
curl -X POST -H "content-type:application/json" "http://localhost:3000/dev/test/" --data '{ "id": 12312312321, "data": {"DID_userid": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389"}}'
```
or
```
curl -X POST -H "content-type:application/json" "http://localhost:3000/dev/test/" --data '{ "id": 12312312321, "data": {"DID_userid": "did:sov:WRfXPg8dantKVubE3HX8pw"}}'
```
# result (example)
```
{
  "jobRunID": 12312312321,
  "data": {
    "didDocument": {
      "@context": "https://w3id.org/did/v1",
      "id": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389",
      "authentication": [
        {
          "type": "Secp256k1SignatureAuthentication2018",
          "publicKey": [
            "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389#controller"
          ]
        }
      ],
      "publicKey": [
        {
          "id": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389#controller",
          "type": "Secp256k1VerificationKey2018",
          "controller": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389",
          "ethereumAddress": "0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389"
        }
      ]
    },
    "content": null,
    "contentType": null,
    "resolverMetadata": {
      "duration": 1720,
      "identifier": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389",
      "driverId": "driver-uport/uni-resolver-driver-did-uport-9",
      "didUrl": {
        "didUrlString": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389",
        "did": {
          "didString": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389",
          "method": "ethr",
          "methodSpecificId": "0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389",
          "parseTree": null,
          "parseRuleCount": null
        },
        "parameters": null,
        "parametersMap": {},
        "path": "",
        "query": null,
        "fragment": null,
        "parseTree": null,
        "parseRuleCount": null
      }
    },
    "methodMetadata": {},
    "result": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389"
  },
  "result": "did:ethr:0xc8f9fa9d07f494e1c9ba79b536138efc7a1d6389",
  "statusCode": 200
}
```
