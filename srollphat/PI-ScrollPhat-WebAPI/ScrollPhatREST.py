import json
import time
from threading import Thread

import scrollphat
import web

urls = (
    '/scroll-string', 'scrollString',
    '/ping', 'ping'
)


def scroll():
    while True:
        scrollphat.scroll()
        time.sleep(0.1)


scrollThread = Thread(target=scroll)


class scrollString:
    def POST(self):
        deserialized = json.loads(web.data())
        scrollphat.write_string(deserialized['message'] + "    ")
        scrollphat.set_brightness(deserialized['brightness'])
        if not scrollThread.is_alive():
            scrollThread.start()


class ping:
    def GET(self):
        return 'pong'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
