from pydantic import BaseModel
#This file is used to define my pydantic request body and response models

# Pydantic models are used to define the structure of the data that we expect to receive in requests and send in responses.
class Blog(BaseModel):
    title :str
    content : str
