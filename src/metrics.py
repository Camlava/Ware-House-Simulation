class Metrics:
    def __init__(self):
        self.fulfillment_times = []

    def record(self, order):
        self.fulfillment_times.append(
            order.completed_time - order.arrival_time
        )

    def average_fulfillment_time(self):
        return sum(self.fulfillment_times) / len(self.fulfillment_times)