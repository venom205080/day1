import requests 
import json 


# get request demo
def get_data():
    res = requests.get("https://api.github.com/users/naveenkrnl")
    # coverts json to python dictionary
    data = json.loads(res.text) 
    return data

def validate_email():
    email = input("enter a email id to check its validity : ")
    url = f"https://api.usebouncer.com/v1.1/email/verify?email={email}"
    
    payload = {}
    headers = {
        'x-api-key': 'GMGzMXYBKQQXgcwxOsQWeNRkJKEi0MpeDdHfJMxw'
    }
    res = requests.request('GET', url, headers=headers, data=payload)

    return json.loads(res.text)


# post request demo
def demo_post_req():
    url = 'https://www.w3schools.com/python/demopage.php'
    payload = {'key': 'value'}
    
    res = requests.Request('POST',url, data=payload)
    return res

if __name__ == '__main__': 
    # response = validate_email()
    # print(response['status'])
    
    res = demo_post_req()
    print(res)