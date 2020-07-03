import requests
import json


url = "http://192.168.1.109/zabbix/api_jsonrpc.php"

payload = {
"jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}

response = requests.post(url, json=payload).json()
print(response)

token = response["result"]

payload = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip"
        ]
    },
    "id": 2,
    "auth": token
}

#response = requests.post(url, json=payload).json()
#print(response)



payload = {
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": "extend",
        "hostids": "10084",
        "sortfield": "name"
    },
    "auth": token,
    "id": 3
}

#response = requests.post(url, json=payload).json()
#print(response)


#for itm in response["result"]:
#    print(itm["itemid"], itm["name"])


payload = {
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": "extend",
        "hostids": "10084",
        "itemids": "23305"
    },
    "auth": token,
    "id": 4
}

response = requests.post(url, json=payload).json()
# print(response)
print(response["result"][0]["name"], response["result"][0]["lastvalue"])

