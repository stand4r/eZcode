from requests import Session

client = Session()
url = "http://127.0.0.1:5000"



#TEST GET /api
#print(client.get(f"{url}/api"))
#print(client.get(f"{url}/api").content)


#TEST GET /api/<int:id>
#print(client.get(f"{url}/api/1"))
#print(client.get(f"{url}/api/1").content)


#TEST POST /api
#print(client.post(f"{url}/api", json = {"link": "http://google.com", "about": "Shit"}))


#TEST PUT /api
#res = client.put(f"{url}/api", json = {"id": 1, "about": "Shit x2"})
#print(res)
#print(res.content)


#TEST DELETE /api
#res = client.delete(f"{url}/api/2")
#print(res)
#print(res.content)
