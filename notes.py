from fastapi import FastAPI


app = FastAPI()#creating an instance of FastAPI

@app.get('/')#1. Created a GET endpoint
def index():
    #For Returning a json response
    return {'message':{'name':'Aaditya'}}

#2. Creating another endpoint
@app.get('/about')
def about():
    return {'message':{'About_Page':'My About Page'}}

#3. Path Parameter in FastAPI
@app.get('/about/{id}')
def about(id:int):
    return {'message':id}

# 4. API Docs
# http://127.0.0.1:8000/docs

#5 Using Query Parameters
'''
http://127.0.0.1:8000/items/?skip=0&limit=10
...the query parameters are:
• skip with a value of 0
limit with a value of 10
I
As they are part of the URL, they are "naturally" strings.
'''

@app.get('/query')
def query(limit:int=10 ,published = True):
    if published:
        return {'data': f'{limit} is published blogs from the database'}
    else:
        return {'data':f'{limit} are all the blogs from the database'}
#6. Request Body
'''To create a body we usually use the the body format
so for creating a body we use the pydantic model , 
1. so we will import BaseModel from pydantic and then create a class that will contain the body format like entities
2. and then we will call this class in the endpoint function
'''
from pydantic import BaseModel
class Blog(BaseModel):
    title:str
    body:str
    published:bool = True
@app.post('/create')
def create_blog(request:Blog):
    return {'data':'Blog is created successfully'}

 