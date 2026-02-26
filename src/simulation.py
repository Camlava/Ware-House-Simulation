import time
from src.entities import Order, Robot
from src.metrics import Metrics

def run_simulation():
    metrics = Metrics()
    robot = Robot(1, "A")

    order = Order(101, ["SKU1"], arrival_time=0)
    time.sleep(1)
    order.completed_time = 1
    metrics.record(order)

    print("Avg Fulfillment Time:", metrics.average_fulfillment_time())