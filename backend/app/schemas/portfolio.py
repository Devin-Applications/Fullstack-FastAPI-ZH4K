from typing import Optional
from pydantic import BaseModel
import uuid

class PortfolioBase(BaseModel):
    title: str
    description: Optional[str] = None

class PortfolioCreate(PortfolioBase):
    user_id: uuid.UUID

class PortfolioUpdate(PortfolioBase):
    title: Optional[str] = None
    description: Optional[str] = None

class Portfolio(PortfolioBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
