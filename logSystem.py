import random

used_id = set('0')


class Vehicle:
    """
    Represent vehicle in logistic system
    Provides information about machine availability
    """

    def __init__(self, vehicle_no):
        """
        Initialize a vehicle
        is_available: bool
        vehicle_no: int
        """
        self.is_available = True
        self.vehicle_no = vehicle_no


class Location:
    """
    Represent location in Order
    Provides information about city and post office
    """

    def __init__(self, city, postoffice):
        """
        Initialize a location
        city: str
        postoffice: int
        """
        self.city = city
        self.postoffice = postoffice


class Item:
    """
    Represent item in Order
    Provides information about price and name
    """

    def __init__(self, name, price):
        """
        Initialize an item
        name: str
        price: float
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns Item in good representation for user
        """
        return 'Your item is {}, price is {} UAH'.format(
            self.name, str(self.price))


class Order:
    """
    Represent order in logistic system
    Provides information about user_name, location. items
    and vehicle for order
    """
    def __init__(self, user_name, city, postoffice, items, vehicle=None):
        """
        Initialize an order
        user_name: str
        location: Location
        items: list of Item
        vehicle: Vehicle
        order_id: int
        """
        self.user_name = user_name
        location = Location(city, postoffice)
        self.location = location
        self.items = items
        self.vehicle = vehicle
        self.order_id = self.create_id()
        print(str(self))

    def create_id(self):
        """
        Generate and return random order_id
        """
        rand_id = 0
        global used_id
        while str(rand_id) in used_id:
            rand_id = random.randint(100000000, 1000000000)
        return rand_id

    def calculate_amount(self):
        price = 0
        for item in self.items:
            price += item.price
        return price

    def __str__(self):
        """
        Returns Order in good representation for user
        """

        return 'Your order number is {}'.format(str(self.order_id))

    def assign_vehicle(self, vehicle):
        """
        Vehicle -> None
        Assigns the car to the order
        """
        if vehicle:
            self.vehicle = vehicle
            vehicle.is_available = False


class LogisticSystem:
    """
    Represent Logistic System
    Provides information about orders and vehicles
    """
    def __init__(self, vehicles, orders=[]):
        """
        Initialize logistic system
        vehicles: list of Vehicle
        orders: list of Order
        """
        self.orders = orders
        self.vehicles = vehicles

    def get_free_vehicle(self):
        """
        Return first free Vehicle in vehicles
        """
        for vehicle in self.vehicles:
            if vehicle.is_available:
                return vehicle

    def place_order(self, order):
        free_vehicle = self.get_free_vehicle()
        if free_vehicle:
            order.assign_vehicle(free_vehicle)
            self.orders.append(order)
        else:
            print("There is no available vehicle to deliver an order.")

    def check_order(self, order_id):
        """
        int -> Order
        Returns order with specific Id, or
        False if there is no such an order
        """
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return False

    def track_order(self, order_id):
        """
        int -> str
        Returns information about specific order
        """
        order = self.check_order(order_id)
        if order:
            if order.vehicle:
                return 'Your order #{} is sent to {}. Total price: {} UAH.'.format(
                    str(order.order_id),
                    order.location.city, str(order.calculate_amount())
                )
            else:
                return "There is no available vehicle to deliver an order."
        else:
            return 'No such order'


if __name__ == '__main__':
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order(user_name='Oleg', city='Lviv',
                     postoffice=53, items=my_items)
    logSystem.place_order(my_order)
    print(logSystem.track_order(my_order.order_id))
    my_items2 = [Item('flowers', 11), Item('shoes', 153),
                 Item('helicopter', 0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    logSystem.place_order(my_order2)
    print(logSystem.track_order(my_order2.order_id))
    my_items3 = [Item('coat', 61.8), Item('shower', 5070),
                 Item('rollers', 700)]
    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    logSystem.place_order(my_order3)
    print(logSystem.track_order(my_order3.order_id))
    print(logSystem.track_order(485932990))
