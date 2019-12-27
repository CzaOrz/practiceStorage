### 这大概算是一个架构问题

#### 背景：
公司一位前端大佬（已离职）的项目，可以简单理解为，网页版微信！

项目只完成了一半，后续也没人接手，领导也不关注，，，就我一个爬虫工程师有点好奇。
但听说原项目是JS实现的，也要不到代码。就只能自己尝试找下python实现websocket服务器的方法。
* Flask-SocketIO：
* Django Channels：
* Tornado：
* ...

因为从事爬虫工作，对Scrapy熟一点，后端框架Flask了解一些

可能是百度出来的案例有点坑，找到的例子要么达不到效果，要么就跑不起来，，，

最后自己只能造轮子，写了一个Pywss，模仿的Flask（用法大致相同）

项目地址：https://github.com/CzaOrz/Pywss

Demo地址：https://czaorz.github.io/Pywss/client

最初只想着实现基本功能，现在基本的功能到是实现了，但在后续拓展上面遇到了大麻烦。

### 问题：
#### 问题1
基于socket编写，手搓的底层WebSocket协议，没有走常规WSGI等接口规范协议，就意味着很多东西都无法适配，，凉凉

#### 问题2
现在都讲究高性能高并发。自己写爬虫也遇到过需要高并发的情况，总的来说，就是需要有额外中间件或管道，
用来传递任务，实现并发。

github上有大致的框架流程图，

### new

python实现websocket服务端，有什么好的关于高并发/集群的框架（项目/方案/论文/博客）

写了一个Pywss，主要目的是想用python快速搭建简易的websocket服务端

项目地址：https://github.com/CzaOrz/Pywss

Demo地址：https://czaorz.github.io/Pywss/client

设计之初受限于知识贫瘠，考虑问题不全面，导致目前仅支持单机部署，，自己挖的坑，，一言难尽。

这些坑暂时不管，后续看情况动刀。目前有两个想法：

1、垂直扩展 -- 异步实现，提升单服务性能。但受限于个人技术，暂时没法实现（不过名字居然被我想好了??还不止一个?? 这可太骚了...，AsyncPywss/AioPywss），不过最近看了asyncio和tornado的源码，虽然很多不懂但还是有所体悟，此方案可行。
2、水平拓展:
本人爬虫工程师，在写爬虫的时候涉及过分布式，大致思想就是，需要有一个中间件或管道，用来调度任务，然后各节点可以从中拿出并执行，获取最终结果。如scrapy-redis。
但websocket
 

### hei
python实现websocket服务端，有什么好的关于高并发/集群的方案（项目/论文/博客）推荐

写了一个Pywss，主要目的是想用python快速搭建简易的websocket服务端
项目地址：https://github.com/CzaOrz/Pywss
Demo地址：https://czaorz.github.io/Pywss/client

在github上面搜了下websocket，其中项目语言，JavaScript最多，Java其次，python也有接近3000多的项目。
看了几个star最多的，一脸懵，再想想我最近看的asyncio和tronado源码，两脸懵。
最后我莫名得出结论，要配一个异步的版本提高性能。

比对下爬虫、http、websocket，不谈实现，只是走下大致流程。
首先，我是搞爬虫的，所以工作中涉及过一些分布式，大致意思就是，
需要有一个中间件或管道（redis），用来调度大量任务，然后各爬虫节点可以从中拿出任务并执行，
获取最终结果。里面很重要的一点是，我的任务，可以被任意节点捕获并执行，如scrapy-redis。
爬虫的分布式逻辑上可能没有特别复杂的地方，如何实现是一个问题。（个人理解，欢迎指正，勿喷）

而http服务器的分布式，如果把一次请求视作一次任务，则多个任务可能会平分到多台节点服务器，和爬虫原理差不多。
但是有些请求需要保留cookie记录，所以他的后续请求，就需要保证还是当前服务器来处理，这个地方就比爬虫的复杂了，
在分配请求的地方还需要做一些处理，保证分配正确。（个人理解，欢迎指正，勿喷）

但websocket是一个长连接，如果说http是由外到内，那websocket更多的是由内到外，不知道这样描述的对不对。
举个不恰当的例子：
某游戏，10台服务器，每台服务器1000个websocket连接，那就相当于1w用户在线
需求1：世界喇叭，发送一条消息给所有用户。要求每台服务器接收请求后各自广播给自己的websocket连接
需求2：私密消息，用户A发送一条消息给B。A所在服务器上报请求，要求服务端快速定位B所在服务器，然后再传递一条数据给B
涉及到一个查找的过程

目前只支持单机部署，

哎，没接触服务端编程，


### hahaha
python实现websocket服务端

在github上面搜了下websocket，其中JavaScript项目最多，Java其次，python也有接近3000多的项目。
有Flask插件、Django插件、tornado等

本着学习的心态，写了Pywss，主要目的是想用python快速搭建简易的websocket服务端
项目地址：https://github.com/CzaOrz/Pywss
Demo地址：https://czaorz.github.io/Pywss/client
