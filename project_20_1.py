# Online Multiplayer Game

import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

clients = []
positions = {}

def handle_client(conn, addr, player_id):
    print(f"Player {player_id} connected from {addr}")
    conn.send(str(player_id).encode())
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            positions[player_id] = data
            broadcast_positions()
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"Player {player_id} disconnected")

def broadcast_positions():
    state = str(positions)
    for client in clients:
        client.send(state.encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print("Server started...")
    player_id = 0
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr, player_id)).start()
        player_id += 1

if __name__ == "__main__":
    main()
