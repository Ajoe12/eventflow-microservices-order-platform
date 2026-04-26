from kafka import KafkaProducer
import json


def get_producer():
    return KafkaProducer(
        bootstrap_servers="localhost:29092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )


def send_order_event(order):
    producer = get_producer()   # 🔥 create here

    event = {
        "order_id": str(order.id),
        "user_id": order.user_id,
        "items": order.items,
        "total_price": order.total_price
    }

    producer.send("order-created", value=event)
    # producer.flush()