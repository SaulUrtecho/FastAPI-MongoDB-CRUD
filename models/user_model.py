from pydantic import BaseModel
from typing import Optional

# here we defined the field types, and these will be required
# these fields are showing in the swagger view for the user input
class UserModel(BaseModel): 
    id: Optional[str] # id is optional
    name: str
    email: str
    password: str
