from collections import Counter


class TrackOrders:
    def __init__(self):
        self.a = list()

    def __len__(self):
        return len(self.a)

    def add_new_order(self, customer, order, day):
        self.a.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        for custom, order, day in self.a:
            if custom == customer:
                orders = list()
                orders.append(order)
        return Counter(orders).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        t_orders = set()

        for custom, order, day in self.a:
            t_orders.add(order)
            if custom == customer:
                l_orders = set()
                l_orders.add(order)
        return t_orders - l_orders

    def get_days_never_visited_per_customer(self, customer):
        t_days = set()

        for custom, order, day in self.a:
            t_days.add(day)
            if custom == customer:
                days = set()
                days.add(day)
        return t_days - days

    def get_busiest_day(self):
        days = list()

        for customer, order, day in self.a:
            if customer == customer:
                days.append(day)

        maximum = max(days, key=days.count)        
        return maximum

    def get_least_busy_day(self):
        for customer, order, day in self.a:
            if customer == customer:
                days = list()
                days.append(day)
        
        minimum = min(days, key=days.count)
        return minimum
