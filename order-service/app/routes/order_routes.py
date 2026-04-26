from fastapi import APIRouter, Depends, HTTPException
from app.schemas import CreateOrder, UpdateOrderStatus
from app.services import order_service
from app.dependencies.auth import get_current_user, require_admin
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

router = APIRouter(prefix="/orders", tags=["Orders"])
security = HTTPBearer()

# 🔹 Create Order (USER)
@router.post("/")
async def create_order(
    data: CreateOrder,
    token: HTTPAuthorizationCredentials = Depends(security),
    user=Depends(get_current_user)
):
    print("in route")
    try:
        return await order_service.create_order(
            user_id=user.get("user_id"),
            data=data,
            token=token.credentials
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# 🔹 Get My Orders
@router.get("/")
async def get_orders(user=Depends(get_current_user)):
    return await order_service.get_orders(user.get("user_id"))


# 🔹 Get Single Order
@router.get("/{order_id}")
async def get_order(order_id: str, user=Depends(get_current_user)):
    order = await order_service.get_order(order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


# 🔹 Update Status (ADMIN)
@router.put("/{order_id}")
async def update_order(
    order_id: str,
    data: UpdateOrderStatus,
    user=Depends(require_admin)
):
    order = await order_service.update_order_status(order_id, data.status)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order