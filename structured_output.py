from typing import Literal
from pydantic import BaseModel, Field, ValidationError

class structured_output(BaseModel):
    category: Literal['billing', 'shipping', 'other']
    priority:int = Field(ge = 1, le = 5)  #here the priority can be from 1 to 5, 


#check function
def check(answer):
    try:
        return structured_output.model_validate_json(answer)  #checking the structure of an output
    except ValidationError:
        return None
    

print(check('{"category":"other","priority":5}'))