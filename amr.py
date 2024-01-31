import requests

value=requests.get("https://gorest.co.in/public/v2/users")
print(value.json())
assert value.status_code ==200, "API is failed"
print("PASS")
ajson={"name":"Tenali Ramakrishna", "gender":"male", "email":"oikjmn@15ce.com", "status":"active"}
adata={
"Content-Type":"application/json",
"Authorization":"Bearer dbb8c457c5e681ee1694d5eed897d3c4bf633461fd6e804a22546189217c2f85"}

value2=requests.post("https://gorest.co.in/public/v2/users", json=ajson, headers=adata)
print(value2.json())

hhjson={"name":"Tenali Ramakrishna", "gender":"male", "email":"eadc@15ce.com", "status":"active"}
lldata={
"Content-Type":"application/json",
"Authorization":"Bearer dbb8c457c5e681ee1694d5eed897d3c4bf633461fd6e804a22546189217c2f85"}
value3=requests.put("https://gorest.co.in/public/v2/users/2138728", json=hhjson, headers=lldata)
print(value3.json())
val=value3.json()
print(val['email'])
