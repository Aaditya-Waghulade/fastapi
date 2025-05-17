from fastapi import FastAPI


app = FastAPI()#creating an instance of FastAPI

@app.get('/')#Created a GET endpoint
def index():
    #For Returning a json response
    return {'message':{'name':'Aaditya'}}

#Creating another endpoint
@app.get('/about')
def about():
    return {'message':{'About_Page':'My About Page'}}