from sqlalchemy.orm import Session
from models import Portfolio
from schemas import PortfolioCreate, PortfolioUpdate
import uuid

def get_portfolio(db: Session, portfolio_id: uuid.UUID):
    return db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()

def get_portfolios_by_user(db: Session, user_id: uuid.UUID, skip: int = 0, limit: int = 100):
    return db.query(Portfolio).filter(Portfolio.user_id == user_id).offset(skip).limit(limit).all()

def create_portfolio(db: Session, portfolio: PortfolioCreate):
    db_portfolio = Portfolio(
        user_id=portfolio.user_id,
        title=portfolio.title,
        description=portfolio.description
    )
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

def update_portfolio(db: Session, portfolio_id: uuid.UUID, portfolio: PortfolioUpdate):
    db_portfolio = db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()
    if db_portfolio:
        db_portfolio.title = portfolio.title
        db_portfolio.description = portfolio.description
        db.commit()
        db.refresh(db_portfolio)
    return db_portfolio

def delete_portfolio(db: Session, portfolio_id: uuid.UUID):
    db_portfolio = db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()
    if db_portfolio:
        db.delete(db_portfolio)
        db.commit()
    return db_portfolio
