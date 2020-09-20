import requests
ploads = {'things':2,'total':25}
r = requests.get('https://httpbin.org/get',params=ploads)
print(r.text)
print(r.url)
