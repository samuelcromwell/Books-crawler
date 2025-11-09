from pydantic import BaseModel, Field
from typing import Optional, List

class Book(BaseModel):
    id: str = Field(alias="_id")
    product_url: str
    name: str
    description: Optional[str] = ""
    category: str
    price_incl_tax: float
    price_excl_tax: float
    availability: str
    num_reviews: int
    image_url: str
    rating: Optional[int]
