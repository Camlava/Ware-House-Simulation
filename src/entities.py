class Order:
    def __init__(self, order_id, location):
        self.order_id = order_id
        self.location = location
        self.fulfillment_time = 0


class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.location = (0, 0)  # Start at origin
        self.total_distance = 0
        self.orders_completed = 0