from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.dependencies import get_sync_db
from app.schemas import Portfolio, PortfolioCreate, PortfolioUpdate
from app.crud import portfolio_crud

router = APIRouter()

@router.post("/portfolios/", response_model=Portfolio)
def create_portfolio(portfolio: PortfolioCreate, db: Session = Depends(get_sync_db)):
    return portfolio_crud.create_portfolio(db=db, portfolio=portfolio)

@router.get("/portfolios/", response_model=List[Portfolio])
def read_portfolios(user_id: uuid.UUID, skip: int = 0, limit: int = 100, db: Session = Depends(get_sync_db)):
    portfolios = portfolio_crud.get_portfolios_by_user(db, user_id=user_id, skip=skip, limit=limit)
    return portfolios

@router.get("/portfolios/{portfolio_id}", response_model=Portfolio)
def read_portfolio(portfolio_id: uuid.UUID, db: Session = Depends(get_sync_db)):
    db_portfolio = portfolio_crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return db_portfolio

@router.put("/portfolios/{portfolio_id}", response_model=Portfolio)
def update_portfolio(portfolio_id: uuid.UUID, portfolio: PortfolioUpdate, db: Session = Depends(get_sync_db)):
    db_portfolio = portfolio_crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio_crud.update_portfolio(db=db, portfolio_id=portfolio_id, portfolio=portfolio)

@router.delete("/portfolios/{portfolio_id}", response_model=Portfolio)
def delete_portfolio(portfolio_id: uuid.UUID, db: Session = Depends(get_sync_db)):
    db_portfolio = portfolio_crud.get_portfolio(db, portfolio_id=portfolio_id)
    if db_portfolio is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio_crud.delete_portfolio(db=db, portfolio_id=portfolio_id)
