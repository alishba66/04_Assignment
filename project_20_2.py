import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

player_id = None
pos = {"x": 0, "y": 0}

def receive_data(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            print("Game state:", data)
        except:
            break

def main():
    global player_id, pos
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    player_id = int(client.recv(1024).decode())
    print(f"You are Player {player_id}")

    threading.Thread(target=receive_data, args=(client,), daemon=True).start()

    while True:
        move = input("Move (w/a/s/d): ").lower()
        if move == 'w':
            pos["y"] -= 1
        elif move == 's':
            pos["y"] += 1
        elif move == 'a':
            pos["x"] -= 1
        elif move == 'd':
            pos["x"] += 1
        client.send(str(pos).encode())

if __name__ == "__main__":
    main()
