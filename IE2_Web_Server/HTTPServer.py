import socket
import os

class HttpRequest:
    CRLF = "\r\n"

    def __init__(self, connection_socket):
        self.socket = connection_socket

    def run(self):
        try:
            self.process_request()
        except Exception as e:
            print(e)

    def process_request(self):
        client_input = self.socket.recv(1024).decode()
        request_lines = client_input.splitlines()
        request_line = request_lines[0]

        # Extract the filename from the request line
        tokens = request_line.split()
        file_name = tokens[1]

        # Prepend a "." so that file request is within the current directory
        file_name = "." + file_name
        print(file_name)

        # Check if the file exists
        file_exists = os.path.isfile(file_name)
        if file_exists:
            print("File here")
            with open(file_name, "rb") as f:
                file_content = f.read()

            status_line = "HTTP/1.0 200 OK" + self.CRLF
            content_type_line = "Content-Type: " + self.content_type(file_name) + self.CRLF
            response_body = file_content
        else:
            print("File not found")
            status_line = "HTTP/1.0 404 Not Found" + self.CRLF
            content_type_line = "Content-Type: text/html" + self.CRLF
            response_body = ("<HTML>" +
                             "<HEAD><TITLE>Not Found</TITLE></HEAD>" +
                             "<BODY>Not Found</BODY></HTML>").encode()

        # Send the HTTP response
        self.socket.sendall(status_line.encode())
        self.socket.sendall(content_type_line.encode())
        self.socket.sendall(self.CRLF.encode())
        self.socket.sendall(response_body)

        # Close the connection socket
        self.socket.close()

    @staticmethod
    def content_type(file_name):
        if file_name.endswith(".htm") or file_name.endswith(".html"):
            return "text/html"
        if file_name.endswith(".ram") or file_name.endswith(".ra"):
            return "audio/x-pn-realaudio"
        return "application/octet-stream"

