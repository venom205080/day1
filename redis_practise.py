import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)


# strings
r.set("name:1", "ramesh")
# print(r.get("name:1"))

# in mset pass a dictionary
r.mset({"name:2": "suresh", "name:3": "mahesh"})
# print(r.get("name:2"))

# working with dates
# import datetime
# today = datetime.date.today()
# visitors = {"dan", "jon", "alex"}
# r.sadd(str(today), *visitors)
# print(visitors)

# set
# fruits = ["apple", "mango", "banana"]
# r.sadd('fruits',"apple")
# r.sadd('')
# print(r.smembers("fruits"))

r.hset('user:1000', 'name', 'John Doe')
r.hset('user:1000', 'email', 'john.doe@example.com')
r.hset('user:1000', 'password', 's3cr3t')
print(r.hget('user:1000', "name"))

# data = {
#     "info" : {
#     "name": "ram",
#     "age": 12,
#     "dept": "logistics"
# }
# }

# r.hset("info", data)
# print(r.hget("info"))