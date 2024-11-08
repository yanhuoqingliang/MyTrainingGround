import argparse
import json

from tornado import websocket, httpserver, ioloop
import tornado
import tornado.web
import tornado.netutil
import tornado.process

from client import ClientDevice

DEVICE_ID = None
H264_HEADER = []
SOCKET_PORT = None
SOCKET_SERVER = None
SOCKET_CLIENT = None


class ScrcpyWSHandler(websocket.WebSocketHandler):
    """scrcpy投屏"""
    DEVICE_CLIENT_DICT = dict()

    def check_origin(self, origin):
        return True

    def initialize(self):
        self.device_id = DEVICE_ID
        self.device_client = None

    async def open(self):
        # 获取当前连接对应的device_client
        print(self.request.path)
        old_device_client = self.DEVICE_CLIENT_DICT.get(self.device_id, None)
        if old_device_client:
            self.device_client = old_device_client
        else:
            self.device_client = self.DEVICE_CLIENT_DICT[self.device_id] = ClientDevice(self.device_id)
        if "screen" in self.request.path:
            self.device_client.ws_client_list.append(self)
            # 重新启动scrcpy 重新开始任务
            async with self.device_client.device_lock:
                await self.device_client.stop()
                await self.device_client.start()
        else:
            self.device_client.ws_touch_list.append(self)

    async def on_message(self, text_data):
        print(self.request.path)
        """receive used to control device"""
        data = json.loads(text_data)
        # touch
        if data['msg_type'] == 2:
            await self.device_client.controller.inject_touch_event(x=data['x'], y=data['y'], action=data['action'])
        # scroll
        elif data['msg_type'] == 3:
            await self.device_client.controller.inject_scroll_event(x=data['x'], y=data['y'],
                                                                    distance_x=data['distance_x'], distance_y=data['distance_y'])
        # swipe
        elif data['msg_type'] == 30:
            await self.device_client.controller.swipe(x=data['x'], y=data['y'], end_x=data['end_x'], end_y=data['end_y'],
                                                      unit=data['unit'], delay=data['delay'])

    def on_connection_close(self):
        if self in self.device_client.ws_client_list:
            self.device_client.ws_client_list.remove(self)
        if self in self.device_client.ws_touch_list:
            self.device_client.ws_touch_list.remove(self)


def start_server():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s",
                        "--serial",
                        help="device serial")
    parser.add_argument("-sp",
                        "--server-port",
                        type=int,
                        help="scrcpy server port")
    args = parser.parse_args()
    global DEVICE_ID
    DEVICE_ID = "123f07fc"

    app = tornado.web.Application([
        (r"/screen", ScrcpyWSHandler),
        (r"/touch", ScrcpyWSHandler),
    ], debug=False)

    http_server = httpserver.HTTPServer(app)
    http_server.listen(20001)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    start_server()
