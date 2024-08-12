from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
import random as r
import redis
import json
rc = redis.Redis(host='localhost', port=6379, decode_responses=True)

# from typing import Annotated

import requests as req

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# function to generate random color
def rand_color():
    return f"rgb({r.randint(0, 255)}, {r.randint(0, 255)}, {r.randint(0, 255)})"

class Register(BaseModel):
    email: str
    password: str

dummy_DB = [{"title": "talk to ashok", "desc":"have to contact ashok to send azure access"}]

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>this is home route nothing is here</h1>"


# path parameters example
@app.get("/users/{id}",response_class=HTMLResponse)
async def get_user(request: Request,id:str):
    URL = "https://jsonplaceholder.typicode.com/users"
    res = req.get(URL).json()
    user_details = res[int(id)-1]
    return templates.TemplateResponse(request=request,name="show_user.html", context={"user": user_details})

# using json
@app.post("/register")
async def register_user(user:Register):
    email = user.email
    password = user.password
    return {
        "msg": "we got data succesfully",
        "email": email,
        "password": password,
    }


# using form
@app.get("/notes", response_class=HTMLResponse)
async def get_notes(request: Request):
    return templates.TemplateResponse(request=request,name="notes.html", context={"notes": dummy_DB, "color": rand_color})

    
@app.post("/notes")
async def set_notes(title: str=Form(), desc: str= Form()):
    dummy_DB.append({"title": title, "desc": desc})
    return RedirectResponse(url="/notes", status_code=303)


@app.get("/photos")
async def get_photos(request: Request):
    cacheValue = rc.get("data")
    if cacheValue:
        return cacheValue
    URL = "https://gist.githubusercontent.com/diondree/92e4518ca7529e1f4d1300993e5cc287/raw/5e689bb33a11a2e55cb11e6f413ddea14c4be804/mock-data-10000.json"
    res = req.get(URL).json()
    await rc.set("data", str(res))
    await rc.expire("data", 100)
    return res


@app.get("/photoswithoutredis")
async def get_photos_without_redis(request: Request):

    URL = "https://gist.githubusercontent.com/diondree/92e4518ca7529e1f4d1300993e5cc287/raw/5e689bb33a11a2e55cb11e6f413ddea14c4be804/mock-data-10000.json"
    res = req.get(URL).json()
    return res

    

    
# query param example
# @app.get("users")
