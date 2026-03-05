CUSTOMERS_LIST = []

def find_customer(customer_id):
    for customer in CUSTOMERS_LIST:
        if customer.customer_id == customer_id:
            return customer
    return None

class Customer:
    def __init__(self, name, customer_id, boards_bought, discount):
        self.name = name
        self.customer_id = customer_id
        self.boards_bought = boards_bought
        self.discount = discount / 100

    def __repr__(self):
        return (f"Customer name: {self.name}\n"
              f"Customer id: {self.customer_id}\n"
              f"Customer discount: {self.discount * 100}%\n")


    def add_customer(self):
        name = input("Enter customer name: ")
        customer_id = int(input("Enter customer id: "))
        boards_bought = int(input("Enter boards bought: "))
        discount = float(input("Enter discount: "))

        new_customer = find_customer(customer_id)
        if new_customer:
            print (f"Customer already exists! Customer name: {new_customer.name}\n")
        else:
            new_customer = Customer(name, customer_id, boards_bought, discount)
            CUSTOMERS_LIST.append(new_customer)
            print ("Customer added!")

    def customer_discount(self, customer_id):
        customer = find_customer(customer_id)
        if not customer:
            print ("Customer not found!")
        else:
            if customer.boards_bought < 10:
                customer.discount = 0.05
            elif 10 <= customer.boards_bought < 50:
                customer.discount = 0.15
            elif 50 <= customer.boards_bought < 100:
                customer.discount = 0.25
            elif customer.boards_bought >= 100:
                customer.discount = 0.5
            print (f'Customer discount: {customer.discount * 100}%')

    def delete_customer(self):
        CUSTOMERS_LIST.remove(self)
        print('Customer deleted!')
