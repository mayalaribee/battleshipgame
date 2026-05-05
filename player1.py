from player_setup import Board

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65535      # The port used by the server
def main():
    print('## Welcome to Battleship!')
    from socket32 import create_new_socket

    with create_new_socket() as s:

        s.bind(HOST, PORT)
        s.listen()
        print("Server started.")
        player1_board = Board(10)
        player2_board = Board(10)


        conn2player, addr = s.accept()
        print('Connected by', addr)
        conn2player.sendall("SETUP")
        var = conn2player.recv()
        if var != "READY":
            print("Client not ready")
            return
        player1_board.ship_place()
        player1_board.ship_place()
        turn = 1
        with conn2player:
            while True:
                if turn == 1:
                    location_row = int(input('Row #:'))
                    location_col = int(input('Column #:'))

                    conn2player.sendall((f"{location_row},{location_col}"))
                    play = conn2player.recv()
                    if not play:
                        break
                    try:
                        location_row = play.split(",")[0]
                        location_col = play.split(",")[1]
                        location_row = int(location_row)
                        location_col = int(location_col)
                    except:
                        continue
                    result = player2_board.mask(location_row, location_col)
                    player2_board.display()
                    conn2player.sendall(f"{location_row},{location_col},{result}")
                    print(result)
                    turn = 2
                else:
                    play = conn2player.recv()
                    if not play:
                        break
                    try:
                        location_row, location_col, result = play.split(",")
                        location_row = int(location_row)
                        location_col = int(location_col)
                    except:
                        continue
                    if result == "hit":
                        player1_board.guess_board[location_row][location_col] = "X"
                        print("Hit!")
                    else:
                        player1_board.guess_board[location_row][location_col] = "O"
                        print("Miss!")
                    player1_board.guess_board.display()
                    print(result)


                    turn = 1
if __name__ == '__main__':

    main()
