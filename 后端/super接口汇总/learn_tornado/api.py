# -*- coding: utf-8 -*-
import os
import tornado.ioloop
import tornado.web

from tornado.options import options, define


class API00(tornado.web.RequestHandler):
    def get(self): self.write("Hello World")


class API01(tornado.web.RequestHandler):
    def get(self): self.write("Hello, this is api-01")


class API02(tornado.web.RequestHandler):
    def get(self, pathname): self.write(f"Hello, this is api-02, and pathname is {pathname or None}")


class API03(tornado.web.RequestHandler):
    def get(self):
        params = self.request.query_arguments  # all params, type is list
        cz = self.get_argument('cza')  # type: str
        cza = self.get_arguments('cza')  # type: list
        self.write(f"Hello, this is api-03, and params is {params}. and cz is {cz}, cza is {cza}")


class API04(tornado.web.RequestHandler):
    def post(self):
        form = self.request.query_arguments
        self.write({'status': 1, 'cza': 'cza', 'form': form})


if __name__ == '__main__':
    define("host", default='127.0.0.1', help="run on the given host")
    define("port", default=8888, help="run on the given port", type=int)
    define("debug", default=False, help="run in debug mode")

    app = tornado.web.Application(
        [
            (r"/", API00),
            (r"/01", API01),
            (r"/02/{0,1}([^/]*)?", API02),  # 似乎一不下心就被写成动态path了
            (r"/03", API03),
            (r"/04", API04)
        ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        # 同源策略 - 所谓同源是指，域名，协议，端口相同。 不同源的客户端脚本(javascript、ActionScript)在没明确授权的情况下，不能读写对方的资源
        # 第三方站点没有访问cookie数据的权限（同源策略）所以我们可以要求每个请求包括一个特定的参数值（XSRF）作为令牌来匹配存储在cookie中的对应值
        xsrf_cookies=True,
        # debug=options.debug,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
