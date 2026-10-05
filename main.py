from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from ArithmeticCalculator import calculate
from fastapi.testclient import TestClient
import unittest
import logging

# Configure logging
logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.DEBUG)

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI application
app = FastAPI()

# Add CORS middleware to allow React frontend to connect
#https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # React's default port
    allow_credentials=True,
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"] # Allow all headers
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

label1txt = "Number 1: "
label2txt = "Number 2: "
resulttxt = "Result: "
@app.get("/")
def read_root():
    return {"message": "Hello, Microservice!"}

@app.post("/operations")
def read_endpoint(data: dict):
    result = calculate(data)
    return result

# CREATE - Add a new item
@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    logging.info("CREATE: %s", item)
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# READ - Get all items
@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    logging.info("GET: %s", items)
    return items

# READ - Get a single item by ID
@app.get("/items/{item_id}", response_model = schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    log_item = schemas.ItemCreate
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    logging.info("GET: %s", log_item)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# UPDATE - Update an existing item
@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    logging.info("PUT: %s", db_item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    for field, value in item.dict().items():
        setattr(db_item, field, value)

    db.commit()
    db.refresh(db_item)
    return db_item

# DELETE - Remove an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    logging.info("DELETE: %s", item.dict)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

message = read_root()

print(message["message"])