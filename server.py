import socket, time, json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Create Listening Socket
server.bind(("127.0.0.1", 5000))
server.listen()

print("Server started...")

messages = [
    {
        "username": "Calum",
        "text": "Hello!"
    },
    {
        "username": "Bob",
        "text": "Hi there!"
    }
]

#Continuely accept new clients
while True:
    #Aceept client socket
    client, address = server.accept()
    print("\n--- New Http Message ---")
    print(f"From: {address}")

    #Read bytes from stream and decode
    request = client.recv(4096)
    request = request.decode()

    #Parse Http Request
    lines = request.split("\r\n")
    method, path, version = lines[0].split(" ")
    print("Method:", method)
    print("Path:", path)


    #Routing
    if path == "/":
        filename = "static/index.html"
        content_type = "text/html"

        with open(filename) as file:
            contents = file.read()

    elif path == "/style.css":
        filename = "static/style.css"
        content_type = "text/css"

        with open(filename) as file:
            contents = file.read()

    elif path == "/script.js":
        filename = "static/script.js"
        content_type = "text/javascript"

        with open(filename) as file:
            contents = file.read()

    elif path == "/messages":
        contents = json.dumps(messages)
        content_type = "application/json"




    

    #Create Response
    response = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Type: {content_type}; charset=UTF-8\r\n\r\n"
        "\r\n" + 
        contents
    )

    #Send back to Socket 
    bytes_response = response.encode()
    client.sendall(bytes_response)
    client.close()