import socket
import threading
from queue import Queue

# 线程之间的运行标志
flag = threading.Event()

# 创建消息队列，用于多线程的通信
data_queue = Queue()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_message(data):
    s.send(data)

def receive_message():
    while not flag.is_set():
        dat = s.recv(32)
        data_queue.put(dat)

try:
    s.connect( ("192.168.43.1", 5000) )
    t = threading.Thread(target=receive_message, daemon=True)
    t.start()
except socket.timeout as error:
    print(f"{error}")
except Exception as error:
    print(f"{error}")
    
