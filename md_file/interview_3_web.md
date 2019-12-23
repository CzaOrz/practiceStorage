### [Web](#Web)
* [TCP握手协议](#TCP握手协议)
* [HTTP](#HTTP)
* [WSGI](#WSGI)
* [MVC](#MVC)
* [Flask](#Flask)
* [Django](#Django)

----------

## web
web应用的本质。客户端发起HTTP请求，服务端接收请求作出回应，比如生成一个Html文件，
然后服务器把此Html文件作为HTTP响应的Body发送给客户端，由客户端进行后续的显示处理。


#### TCP握手协议


#### HTTP
HTTP是一种文本协议，也是常用的网络通信协议。

一次HTTP事件，包含Header和Body。事件通常分为请求事件和响应事件。

请求事件Header中，主要报头和报文。Body是根据请求方式的可选事件
* **GET / HTTP/1.1** 报头包含请求方式、请求路径、协议版本
* **Host: www.google.com** 报文则由Key:Value的结构组成

响应事件Header中，也包括报头和报文，Body就是我们在浏览器中能看到的内容
* **HTTP/1.1 200 OK** 响应报头中包含协议版本、响应状态码、信息说明
* **X-Powered-By: Express** 报文则一样，由Key:Value的结构组成

Header之间以\r\n进行划分，出现两个\r\n\r\n，则后面的数据全为body。

200成功、3xx重定向、4xx客户端异常、5xx服务端异常


#### WSGI
**Web-Server-Gateway-Interface** web服务器网关接口

最简单的web应用就是先把html文件保存好，用先有的HTTP服务器接受用户请求，然后直接返回已有的html文件。
这就是我们常说的静态服务器，如Nginx等。

而实际上一个web应用可能复杂的多，需要我们获取HTTP请求信息并解析，然后做出对应的处理再打包返回。
故为了简化开发，WSGI接口出现了。他实现了对HTTP请求的初步包装，以便web应用进行后续的处理。

一个WSGI接口，封装HTTP请求后，会为web应用提供两个参数，分别为environ和start_response。
* **environ** 此参数是一个dict对象，包含有完整的HTTP请求信息
* **start_response** 此参数是一个函数对象，是用于发送HTTP响应报文的函数

web应用，从WSGI接口中获取这两个参数并进行后续的处理，业务逻辑完成后。
调用且仅能调用一次start_response函数，用于返回响应报文
```start_response("200 fucking", [("Content-Type", "this/is/a/joking")])```，
此函数接受两个参数，第一个是响应报头，里面包含状态码和信息说明。第二个是响应报文，是一个list，
子元素是tuple，tuple内部为两个string，分别对应着报文中的Key:Value
```
from wsgiref.simple_server import make_server
def test_app(environ, start_response):
    start_response("200 fucking-man", [("Content-Type", "text/html")])
    return [b"hello, funking man"]
web = make_server("", 8888, test_app)
web.serve_forever()
```


#### MVC
Model-View-Controller —— 模型-视图-控制器

python后端代码中，负责处理路由的函数或者类，就是控制器，主要负责业务逻辑

而像jinjia2或Django自带模板框架，里面一些带有{{}}特殊变量的文件，就是视图，主要负责显示逻辑。
也就是通过一些简单的替换，生成最终的显示页面。

而业务逻辑 传递给 显示逻辑 的部分，即是Model模板。本质上是一个字典，也是一个映射表。
作用还是为了渲染视图，生成目标模板

MVC架构，初步拆离了业务逻辑与显示逻辑。


#### Flask


#### Django