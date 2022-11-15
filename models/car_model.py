from pydantic import BaseModel, HttpUrl
from typing import Optional

# here we defined the field types, and these will be required
# these fields are showing in the swagger view for the user input
class CarModel(BaseModel): 
    id: Optional[str] # id is optional
    url: HttpUrl
    model: str
    color: str
    year: str
