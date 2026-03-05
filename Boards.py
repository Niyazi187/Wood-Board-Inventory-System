from Customers import find_customer

BOARDS_LIST = []

def find_board(board_id):
    for board in BOARDS_LIST:
        if board.board_id == board_id:
            return board
    return None

class Board:
    def __init__(self, name, board_length, board_width, factory, board_id, count, price):
        self.name = name
        self.board_length = board_length
        self.board_width = board_width
        self.factory = factory
        self.board_id = board_id
        self.count = count
        self.size = board_width * board_length
        self.price = price

    def __repr__(self):
        return (f"\nBoard name: {self.name}\n"
              f"Board id: {self.board_id}\n"
              f"Board count: {self.count}\n"
              f"Board size: {self.size}\n"
              f"Board Factory: {self.factory}\n"
              f"Board price: {self.price}\n")

    def add_board(self):
        name = input("Enter board name: ")
        board_length = float(input("Enter board length in centimeters: "))
        board_width = float(input("Enter board width in centimeters: "))
        factory = input("Enter board factory: ")
        board_id = int(input("Enter board id: "))
        count = int(input("Enter count: "))
        price = float(input("Enter price: "))

        new_board = find_board(board_id)

        if new_board:
            print(f'Board already exists! Board name: {new_board.name}')
        else:
            new_board = Board(name, board_length, board_width, factory, board_id, count, price)
            BOARDS_LIST.append(new_board)
            print("New board added!")

    def rename_board(self,new_name):
        self.name = new_name

    def rename_factory(self, new_factory):
        self.factory = new_factory

    def board_info(self, board_id):
        board = find_board(board_id)
        if board:
            print(board)
        else:
            print("Board not found!")

    def new_stock_arrived(self, amount):
        self.count += amount

    def delete_board(self):
        BOARDS_LIST.remove(self)
        print("Board deleted!")

    def selling_boards(self, board_id, customer_id, count):
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
            board.price = (board.price * (1 - customer.discount)) * count
            print(f"Board selling!\nBoards left: {board.count}\nPrice: {board.price:.2f}")


