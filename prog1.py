import requests
req1=raw_input('Enter the URL you want to scrape: ')
req = requests.get(req1)
 
print(req.encoding)     
print(req.status_code) 
print(req.elapsed)     
print(req.url)         
print(req.history)     
print(req.headers['Content-Type'])

