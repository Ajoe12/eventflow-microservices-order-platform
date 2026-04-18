from app.models import Item
from fastapi import HTTPException

#create item(ADMIN)
async def create_item(data):
    #Item(data.dict()) Item({key:value})
    #Item(key:value) => this is what it requires
    try:
        item = Item(**data.dict())
        await item.insert()
        return item
    except Exception as e:
        raise HTTPException(status_code=500,detail="Failed while creating the item")

#get single items
async def get_item(item_id: str):
    try:
        return await Item.get(item_id)
    except Exception:
        raise HTTPException(status_code=500,detail="failed while fecthing item")

#delete single Item
async def delete_item(item_id: str):
    try:
        item = await Item.get(item_id)
        if not item:
            return None
        await item.delete()
        return True
    except Exception:
        raise HTTPException(status_code=500,detail="failed while deleting item")

#update single Item
async def update_item(item_id: str,data):
    try:
        item = await Item.get(item_id)
        if not Item:
            return None

        updated_data = data.dict(exclude_unset=True)
        
        for key,val in updated_data.items():
            setattr(item,key,val)
        
        await item.save()
        return item
    except:
        raise HTTPException(status_code=500,detail="failed while updating the data")

#get items (pagination + filtering)
async def get_items(page: int, limit: int,name: str = None):
    try:
        query={}

        if name:
            #name = lap => fetches laptop, LAPTOP, lapdesk....
            #$options: "i" → case-insensitive
            query["name"] = {"$regex": name,"$options":"i"}
        
        #page=2 limit=10
        #skip (2-1)*10 => skips first 10 records
        #only returns 10 items
        items = await Item.find(query).skip((page-1)*limit).limit(limit).to_list()
        return items
    except Exception:
        raise HTTPException(status_code=500,detail="failed while fetching the data")