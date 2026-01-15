from pydantic import BaseModel, Field

class CreateProductRequest(BaseModel):
    name: str = Field(min_length=3)
    category: str = Field(min_length=3)
    price: float = Field(gt=0)
    description: str | None = None
    in_stock: bool = True

class UpdateProductRequest(BaseModel):
    name: str | None = Field(default=None, min_length=3)
    category: str | None = Field(default=None, min_length=3)
    price: float | None = Field(default=None, gt=0)
    description: str | None = None
    in_stock: bool | None = None
