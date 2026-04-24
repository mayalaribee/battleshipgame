
from socket32 import create_new_socket
HOST = '127.0.0.1'
PORT = 65432
def main():

    with create_new_socket() as s:

        #Bind socket to address and publish contact info
        s.bind(HOST, PORT)
        s.listen()
        print("ROSHAMBO server started. Listening on", (HOST, PORT))
        import roshambo3_2p_client as rlib
        conn2client, addr = s.accept()
        print('Connected by', addr)

        # Answer incoming connection

        with conn2client:
            while True: # message processing loop
                choice = conn2client.recv()
                if choice == '':
                    break

                chosen_decision = rlib.player_choice()
                conn2client.sendall(chosen_decision)

if __name__ == '__main__':
    main()
