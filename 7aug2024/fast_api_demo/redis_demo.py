import redis
import requests as req
rc = redis.Redis(host='localhost', port=6379, decode_responses=True)


# async def func():
#     if(rc.get("data")):
#         print(rc.get("data"))
#     URL = "https://gist.githubusercontent.com/diondree/92e4518ca7529e1f4d1300993e5cc287/raw/5e689bb33a11a2e55cb11e6f413ddea14c4be804/mock-data-10000.json"
#     res = req.get(URL).json()
#     await rc.set("data", res)
#     await rc.expire("data", 60)
#     print(rc.get("data"))
    
# func()
# URL = "https://gist.githubusercontent.com/diondree/92e4518ca7529e1f4d1300993e5cc287/raw/5e689bb33a11a2e55cb11e6f413ddea14c4be804/mock-data-10000.json"
# res = req.get(URL).json()
# rc.set("data", res)
# rc.expire("data", 60)
# print(rc.get("data"))