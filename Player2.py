
from player_setup import Board
HOST = '127.0.0.1'
PORT = 65535
def main():
    from socket32 import create_new_socket
    with create_new_socket() as s:
        #Bind socket to address and publish contact info
        s.connect(HOST, PORT)
        print("Battleship server started. Listening on", (HOST, PORT))
        player2_board = Board(10)
        signal = s.recv()

        if signal == "SETUP":
            player2_board.ship_place()
            player2_board.ship_place()

            s.sendall("READY")

        # Answer incoming connection
        while True:
            location_row = int(input('Row #:'))
            location_col = int(input('Column #:'))
            s.sendall((f"{location_row},{location_col}"))

            decision = s.recv()
            if not decision:
                break
            try:
                location_row, location_col, result = decision.split(",")
                location_row = int(location_row)
                location_col = int(location_col)
            except:
                continue
            if result == "hit":
                player2_board.guess_board[location_row][location_col] = "X"
                print("Hit!")
            else:
                player2_board.guess_board[location_row][location_col] = "O"
                print("Miss!")
            print(decision)
            player2_board.display()

if __name__ == '__main__':
    main()
