from fastapi import Depends, APIRouter, HTTPException
from app.dependencies.auth import get_current_user, require_admin
from app.services import item_service
from app.schemas import UpdateItem,CreateItem, ItemResponse

router = APIRouter(prefix="/items",tags=["items"])

#create item (ADMIN ONLY)
@router.post("/")
async def createItem(data: CreateItem, user = Depends(require_admin)):
    return await item_service.create_item(data)
        
    
#get items(pagination and filtering)
@router.get("/")
async def get_items(page:int = 1,limit:int=10,name: str = None,user=Depends(get_current_user)):
    return await item_service.get_items(page,limit,name)


#get single item
@router.get("/{item_id}")
async def get_item(item_id:str,user=Depends(get_current_user)):
    item = await item_service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404,detail="Item not found")
    return item

#update Item(ADMIN ONLY)
@router.put("/{item_id}")
async def update_item(item_id:str,data:UpdateItem,user=Depends(require_admin)):
    item = await item_service.update_item(item_id,data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

#delete item(ADMIN ONLY)
@router.delete("/{item_id}")
async def delete_item(item_id:str,user=Depends(require_admin)):
    success = await item_service.delete_item(item_id)

    if not success:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Item deleted successfully"}