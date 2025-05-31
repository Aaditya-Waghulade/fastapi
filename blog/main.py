from fastapi import FastAPI
import schemas
import models
from database import engine , Base

  # Importing the pydantic Blog model from schemas.py

app = FastAPI()

#1 . Creating Body of Pydantic Model so that we would be able to pass them into the function and then the funtion will return it to us
#Pydantic Model is created into the schemas.py file then we will import it here and will use it in the function

#2. Creating a POST endpoint to create a blog
@app.post("/blog")
def create(request:schemas.Blog):
    return request

#So now the class Blog is created and have the attributes title, content and author and then this entities are passed to the function create and then the function will return the data in the form of json response , After Performing BaseModel we got the rquest body and response in the form of json

#3. Database Connection and complete explaination is given in the database.py file
#4.After  database.py create model.py for creating table structure and then import it into main.py(models.py)

#5. Now create a table in the database using the Base.metadata.create_all(engine) method
models.Base.metadata.create_all(engine)
