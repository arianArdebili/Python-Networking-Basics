# Python Socket Programming — Simple Client & Server

This project demonstrates a basic example of socket programming in Python.  
It creates a simple **TCP server** that listens for incoming connections and sends a welcome message to any connected **client**.

---

## 🖥️ Server (server.py)
- Binds to `0.0.0.0` (listens on all interfaces)
- Accepts incoming connections
- Sends a welcome message to each client

```bash
python server.py
