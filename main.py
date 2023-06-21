from fastapi import FastAPI,status,HTTPException
import logging
import models
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import SessionLocal
from pydantic import ValidationError


   

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("This Message for Debug ")
logging.warning("This is the Warring Message ")
logging.error("This is the Error Define")
logging.critical("This Message is Critical")

app = FastAPI()


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Item(OurBaseModel):
    id: int
    name: str
    price: int

db=SessionLocal()

@app.get("/items",response_model=list[Item])
def getall_Item():
    # db=SessionLocal()
    getallItem = db.query(models.Item).all()
    return getallItem



@app.post("/additem",response_model=Item)
def create(item:Item):
    # db=SessionLocal()
    newitem=models.Item(
        id=item.id,
        name=item.name,
        price=item.price
    ) 
    find_item=db.query(models.Item).filter(models.Item.id==item.id).first()
    if find_item is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="alredy used id")

    db.add(newitem)
    db.commit()
    # db.refresh(newitem)
    return newitem

@app.put('/update_item/{item_id}',response_model=Item)
def update_item(item_id:int,item:Item):
    find_item=db.query(models.Item).filter(models.Item.id==item_id).first()
    # db=SessionLocal()
    find_item.id=item.id
    find_item.name=item.name
    find_item.price=item.price
    db.commit()
    # db.refresh()  
    return find_item


@app.delete("/Delete_item/{item_id}",response_model=Item,status_code=200)
def delete_item(item_id:int):
    find_item=db.query(models.Item).filter(models.Item.id==item_id).first()
    db.delete(find_item)
    db.commit()
    return find_item












 




    
  