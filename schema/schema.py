from typing import Optional
from pydantic import BaseModel

class PostSchema(BaseModel):
    title   :   str
    content :   str
    publish :   bool    =   True
    # rating  :   Optional[int]   =   None
