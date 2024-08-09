
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class OrderQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return "Queue is empty!"
        dequeued_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return "Queue is empty!"
        return self.head.data


class CustomerOrder:
    def __init__(self, order_id, waiting_time, complexity):
        self.order_id = order_id
        self.waiting_time = waiting_time
        self.complexity = complexity

class CustomerOrderQueue:
    def __init__(self):
        self.orders = []

    def add_order(self, order_id, waiting_time, complexity):
        order = CustomerOrder(order_id, waiting_time, complexity)
        self.orders.append(order)
        self.orders.sort(key=lambda x: (x.waiting_time, x.complexity))

    def process_order(self):
        if not self.orders:
            return "No orders to process!"
        return self.orders.pop(0)

    def notify_customer(self, order):
        print(f"Order {order.order_id} is ready for pickup or delivery.")

# Task 5

kitchen_queue = OrderQueue()
kitchen_queue.enqueue("Order 1")
kitchen_queue.enqueue("Order 2")
kitchen_queue.enqueue("Order 3")

print("Kitchen Queue:")
while not kitchen_queue.is_empty():
    print(kitchen_queue.dequeue())

customer_queue = CustomerOrderQueue()
customer_queue.add_order("Order A", 5, 2)
customer_queue.add_order("Order B", 3, 1)
customer_queue.add_order("Order C", 4, 3)

print("\nCustomer Order Queue:")
while customer_queue.orders:
    order = customer_queue.process_order()
    customer_queue.notify_customer(order)