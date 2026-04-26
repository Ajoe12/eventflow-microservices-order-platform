from kafka import KafkaConsumer
import json
import asyncio

from app.models import Item

# 🔹 Async DB logic
async def handle_order_event(event):
    for item in event["items"]:
        item_id = item["item_id"]
        quantity = item["quantity"]

        print(f"🔻 Reducing stock for {item_id} by {quantity}")

        db_item = await Item.get(item_id)

        if not db_item:
            print(f"❌ Item {item_id} not found")
            continue

        # 🔥 Reduce stock
        db_item.quantity -= quantity

        if db_item.quantity < 0:
            print(f"⚠️ Stock went negative for {item_id}, setting to 0")
            db_item.quantity = 0

        await db_item.save()
        print(f"✅ Updated stock for {item_id}: {db_item.quantity}")


# 🔹 Sync wrapper (thread-safe)
def handle_order_event_sync(event):
    try:
        asyncio.run(handle_order_event(event))
    except Exception as e:
        print("❌ Error processing event:", e)


# 🔹 Kafka consumer loop
def start_consumer():
    consumer = KafkaConsumer(
        "order-created",
        bootstrap_servers="localhost:29092",  # 🔥 IMPORTANT (your setup)
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        group_id="item-service-group"
    )

    print("🚀 Kafka Consumer Started...")

    for message in consumer:
        event = message.value
        print("📩 Received event:", event)

        handle_order_event_sync(event)