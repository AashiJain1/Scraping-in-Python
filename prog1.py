import requests
req1=input('Enter the URL you want to scrape: ')
try:
    req=requests.get(req1)
    print(req.encoding)     
    print(req.status_code) 
    print(req.elapsed)     
    print(req.url)         
    print(req.history)     
    print(req.headers['Content-Type'])
except:
    print('Invalid URL')
