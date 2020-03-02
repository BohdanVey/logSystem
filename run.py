import logSystem


class Menu:
    def __init__(self):
        text = 'Print number of vehicles: '
        number_of_vehicles = int(input(text))
        vehicles = [logSystem.Vehicle(i) for i in range(number_of_vehicles)]
        self.LogisticSystem = logSystem.LogisticSystem(vehicles)

    def track(self):
        """
        Print information about order
        """
        order = int(input('Print orderId: '))
        print(self.LogisticSystem.track_order(order))
    def add(self):
        """
        Add new order
        """

        user_name = input('Print user name: ')
        city = input('Print city: ')
        post_oficce = input('Print post office: ')
        number = input('Print number of Item: ')
        items = []
        for i in range(int(number)):
            name = input('Print name of item: ')
            price = float(input('Print price of item: '))
            items.append(logSystem.Item(name, price))
        order = logSystem.Order(user_name, city, post_oficce, items)
        self.LogisticSystem.place_order(order)

    def menu(self):
        print(
            """Print 'add' to add new order
Print 'track' to track your order
Print 'quit' to quit"""
        )
        read = input().lower().strip()
        if read == 'add':
            self.add()
        elif read == 'track':
            self.track()
        elif read == 'quit':
            print('Thanks for using my program')
            return
        else:
            print('The {} is incorrect input'.format(read))
        self.menu()


if __name__ == '__main__':
    menu = Menu()
    menu.menu()
