# Cloud Database Client  

## 📌 Project Description  
This project implements a simple **TCP client** that connects to a remote **echo server**.  
It provides a **command-line interface (CLI)** that allows users to establish a connection, send messages, and receive responses in real time.  

The application is fully containerized using **Docker**, ensuring easy setup, portability, and consistent behavior across different environments.  

## ⚙️ Features  
- Connect and disconnect from a server using hostname and port  
- Send messages to the server and receive echoed responses  
- Interactive CLI with commands:  
  - `connect` → connect to a server (`server + port`)  
  - `disconnect` → disconnect from the current server  
  - `send` → send a message to the server  
  - `help` → show available commands  
  - `quit` → exit the program  
- Error handling for invalid commands or connection issues  
- Lightweight Docker container for easy deployment  

## 🚀 Getting Started  

### 1. Build the Docker image  
```bash
docker build -t cloud-db-client .
```

### 2. Run the container  
```bash
docker run -it cloud-db-client
```

This will launch the interactive CLI inside the container.  

## 🖥️ Example Usage  
```bash
EchoClient> connect cdb.dis.cit.tum.de 5551
Connection to MSRG Echo server established: / cdb.dis.cit.tum.de / 5551  

EchoClient> send Hello World
Hello World  

EchoClient> disconnect
Connection terminated: /cdb.dis.cit.tum.de / 5551
```

## 📂 Project Structure  
```
├── client.py        # Main TCP client implementation
├── Dockerfile       # Docker build instructions
├── requirements.txt # Python dependencies
├── run              # Script to build and run the client in Docker
```

## 🔮 Future Improvements  
- Add logging for better debugging and monitoring  
- Handle automatic reconnections if the server goes down  
- Support for multiple concurrent connections  
- Extend listener mode for real-time incoming messages  
- Configurable environment variables for server and port  