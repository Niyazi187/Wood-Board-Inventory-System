BOARDS_LIST = []
CUSTOMERS_LIST = []

def find_board(board_id):
    for board in BOARDS_LIST:
        if board.board_id == board_id:
            return board
    return None

def find_customer(customer_id):
    for customer in CUSTOMERS_LIST:
        if customer.customer_id == customer_id:
            return customer
    return None

class Board:
    def __init__(self, name, board_length, board_width, factory, board_id, count):
        self.name = name
        self.board_length = board_length
        self.board_width = board_width
        self.factory = factory
        self.board_id = board_id
        self.count = count
        self.size = board_width * board_length

def add_board():
    name = input("Enter board name: ")
    board_length = float(input("Enter board length in centimeters: "))
    board_width = float(input("Enter board width in centimeters: "))
    factory = input("Enter board factory: ")
    board_id = input("Enter board id: ")
    count = int(input("Enter count: "))

    new_board = find_board(board_id)

    if new_board:
        print(f'Board already exists! Board name: {new_board.name}\n')
    else:
        new_board = Board(name, board_length, board_width, factory, board_id, count)
        BOARDS_LIST.append(new_board)
        print("New board added!")


def rename_board(board_id ,new_name):
    board = find_board(board_id)
    if board:
        board.name = new_name
        print("Board renamed!")
    else:
        print("Board not found!")

def rename_factory(board_id, new_name):
    board = find_board(board_id)
    if board:
        board.factory = new_name
        print("Factory renamed!")
    else:
        print("Board not found!")


def board_info(board_id):
    board = find_board(board_id)
    if board:
        print(f"Board name: {board.name}\n"
              f"Board id: {board.board_id}\n"
              f"Board count: {board.count}\n"
              f"Board size: {board.size}\n"
              f"Board Factory: {board.factory}\n")
    else:
        print("Board not found!")

def new_stock_arrived(board_id, count):
    board = find_board(board_id)
    if board:
        board.count = board.count + count
        print(f"New stock arrived! Count: {board.count}")
    else:
        print("Board not found!")

def delete_board(board_id):
    board = find_board(board_id)
    if not board:
        print('Board not found!')
    else:
        BOARDS_LIST.remove(board)


class Customer:
    def __init__(self, name, customer_id, boards_bought, discount):
        self.name = name
        self.customer_id = customer_id
        self.boards_bought = boards_bought
        self.discount = discount

def add_customer(name, customer_id, boards_bought, discount):
    name = input("Enter customer name: ")
    customer_id = input("Enter customer id: ")
    boards_bought = int(input("Enter boards bought: "))
    discount = float(input("Enter discount: "))

    new_customer = find_customer(customer_id)
    if new_customer:
        print(f"Customer already exists! Customer name: {new_customer.name}\n")
    else:
        new_customer = Customer(name, customer_id, boards_bought, discount)
        CUSTOMERS_LIST.append(new_customer)
        print("Customer added!")


def customer_discount(customer_id):
    customer = find_customer(customer_id)
    if not customer:
        print("Customer not found!")
    else:
        if customer.boards_bought < 10:
            customer.discount = 0.05
        elif customer.boards_bought >= 10 and customer.boards_bought < 50:
            customer.discount = 0.15
        elif customer.boards_bought >= 50 and customer.boards_bought < 100:
            customer.discount = 0.25
        elif customer.boards_bought >= 100:
            customer.discount = 0.5
        print(f'Customer discount: {customer.discount * 100}%')


def customer_info(customer_id):
    customer = find_customer(customer_id)
    if customer:
        print(f"Customer name: {customer.name}\n"
              f"Customer id: {customer.customer_id}\n"
              f"Customer discount: {customer.discount * 100}%\n")
    else:
        print('Customer not found!')

def delete_customer(customer_id):
    customer = find_customer(customer_id)
    if not customer:
        print("Customer not found!")
    else:
        CUSTOMERS_LIST.remove(customer)

def selling_boards(board_id, customer_id, count):
    board = find_board(board_id)
    customer = find_customer(customer_id)

    if not board:
        print("Board not found!")
    elif not customer:
        print("Customer not found!")
    elif board.count < count:
        print("Board not enough!")
    else:
        customer.boards_bought += count
        board.count = board.count - count
        print(f"Board selling!\n Boards left: {board.count}")
