import tornado.web
import tornado.websocket
import tornado.ioloop


# 定义 WebSocket 处理程序
class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket连接已建立")

    def on_message(self, message):
        print("收到客户端消息：" + message)
        # 处理收到的消息
        self.write_message("返回服务端消息：" + message)

    def on_close(self):
        print("WebSocket连接已关闭")


# 创建应用程序并定义路由
app = tornado.web.Application([
    (r"/ws", WebSocketHandler),
])

# 启动服务器并监听端口
if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

