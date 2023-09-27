import socket
import threading
import HTTPServer

class WebServer:
    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("", port))
        self.server_socket.listen(1)
        print(f"WebServer is listening on port {port}")

    def run(self):
        while True:
            connection_socket, address = self.server_socket.accept()
            request = HTTPServer(connection_socket)
            client_thread = threading.Thread(target=request, args=(connection_socket,))
            client_thread.start()

if __name__ == "__main__":
    PORT = 10000  # default port
    server = WebServer(PORT)
    server.run()
