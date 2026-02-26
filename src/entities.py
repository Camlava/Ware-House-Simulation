class Order:
    def __init__(self, order_id, items, arrival_time):
        self.order_id = order_id
        self.items = items
        self.arrival_time = arrival_time
        self.completed_time = None


class Robot:
    def __init__(self, robot_id, start_node):
        self.robot_id = robot_id
        self.position = start_node
        self.busy = False


class InventoryItem:
    def __init__(self, sku, quantity, reorder_point, reorder_qty):
        self.sku = sku
        self.quantity = quantity
        self.R = reorder_point
        self.Q = reorder_qty