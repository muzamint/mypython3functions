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
➜  mypython3functions (master) ✗ curl -X POST -H "content-type:application/json" "http://localhost:3000/dev/first/" --data '{ "id": 12312312321, "data": {"base": "ETH", "quote": "USD"}}'

{"jobRunID": 12312312321, "data": {"USD": 343.18, "result": 343.18}, "result": 343.18, "statusCode": 200}%   ➜  mypython3functions (master) ✗ curl -X POST -H "content-type:application/json" "https://scalewaypython3b4jyscy3-first.functions.fnc.fr-par.scw.cloud/" --data '{ "id": 12312312321, "data": {"base": "ETH", "quote": "USD"}}'
```
# result (example)
```
{"jobRunID": 12312312321, "data": {"USD": 344.63, "result": 344.63}, "result": 344.63, "statusCode": 200}
```
