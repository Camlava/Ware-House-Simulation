import random
import math
from src.entities import Order, Robot

class WarehouseSimulation:
    def __init__(self, num_robots=3, num_orders=20):
        self.num_robots = num_robots
        self.num_orders = num_orders
        self.robots = [Robot(robot_id=i) for i in range(num_robots)]
        self.orders = []
        self.completed_orders = []
        self.total_distance = 0

    def generate_orders(self):
        for i in range(self.num_orders):
            # Random (x, y) location inside 10x10 grid
            location = (random.randint(0, 10), random.randint(0, 10))
            self.orders.append(Order(order_id=i, location=location))

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def assign_orders(self):
        for order in self.orders:
            robot = min(self.robots, key=lambda r: self.distance(r.location, order.location))
            travel_distance = self.distance(robot.location, order.location)

            robot.location = order.location
            robot.total_distance += travel_distance
            robot.orders_completed += 1

            order.fulfillment_time = travel_distance  # proportional model
            self.total_distance += travel_distance
            self.completed_orders.append(order)

    def compute_metrics(self):
        avg_fulfillment = sum(o.fulfillment_time for o in self.completed_orders) / len(self.completed_orders)
        robot_utilization = sum(r.orders_completed for r in self.robots) / (self.num_orders)
        avg_distance = self.total_distance / self.num_orders

        return avg_fulfillment, robot_utilization, avg_distance

    def run(self):
        print("Simulation started...")
        self.generate_orders()
        self.assign_orders()
        avg_fulfillment, robot_utilization, avg_distance = self.compute_metrics()

        print(f"Total Orders: {self.num_orders}")
        print(f"Average Fulfillment Time: {round(avg_fulfillment, 2)}")
        print(f"Robot Utilization: {round(robot_utilization * 100, 1)}%")
        print(f"Average Travel Distance: {round(avg_distance, 2)}")
        print("Simulation completed.")

def run_simulation():
    sim = WarehouseSimulation()
    sim.run()