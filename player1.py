from socket32 import create_new_socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def main():
    print('## Welcome to Battleship!')

    with create_new_socket() as s:
        s.bind(HOST, PORT)
        s.listen()
        print("Server started.")
        import Player2 as rlib
        conn2player, addr = s.accept()
        print('Connected by', addr)
    with conn2player:
        while True:
            play = conn2player.recv()
            if choice == '':
                break
            player_choice = rlib.#function that defines how the player makes their choice
            conn2player.sendall(player_choice)

        #create my game loop
while True:
    small_ship = '***'
    large_ship = '*****'
    if ship_choice == input('Please choose your first ship you would like to place:'):
        break
    if input != 'small_ship' or 'large_ship':
        print('Value must be a ship name, please try again')


        s.sendall(str(guess))
        response = s.recv()
        print(response)

if __name__ == '__main__':
    main()
