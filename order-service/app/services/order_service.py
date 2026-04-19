from app.models import Order
from app.core.config import ITEM_SERVICE_URL
from app.utils.http_client import get_item

# 🔹 Create Order
from app.models import Order
from app.core.config import ITEM_SERVICE_URL
from app.utils.http_client import get_item


async def create_order(user_id: str, data,token:str):
    total_price = 0
    validated_items = []

    for item in data.items:
        # 🔹 Call item service
        item_data = await get_item(item.item_id, ITEM_SERVICE_URL,token)

        if not item_data:
            raise Exception(f"Item {item.item_id} not found")

        # 🔹 Stock validation
        if item.quantity > item_data.get("quantity", 0):
            raise Exception(f"Insufficient stock for item {item.item_id}")

        # 🔹 Price calculation
        price = item_data.get("price", 0)
        total_price += price * item.quantity

        validated_items.append({
            "item_id": item.item_id,
            "quantity": item.quantity,
            "price": price
        })

    # 🔹 Create order
    order = Order(
        user_id=user_id,
        items=validated_items,
        total_price=total_price,
        status="PENDING"
    )

    await order.insert()
    return order


# 🔹 Get Orders for User
async def get_orders(user_id: str):
    return await Order.find(Order.user_id == user_id).to_list()


# 🔹 Get Single Order
async def get_order(order_id: str):
    return await Order.get(order_id)


# 🔹 Update Order Status (ADMIN)
async def update_order_status(order_id: str, status: str):
    order = await Order.get(order_id)

    if not order:
        return None

    order.status = status
    await order.save()

    return order