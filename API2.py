# import requests
#
# head = {
#     "accept": "text/plain",
#     "Content-Type": "application/json"
# }
# payload = {
#     "id": 1454,
#     "title": "amritha",
#     "dueDate": "2024-01-26T09:19:26.157Z",
#     "completed": True
# }
#
# response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json=payload)
# print(response.status_code)
# print(response.json())
# data = response.json()
# print(data["id"])
# assert data["id"] == 1454
