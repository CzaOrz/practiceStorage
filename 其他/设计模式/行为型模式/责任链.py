class Request:
    num = 1


class Handler:
    def process(self, request: Request): raise NotImplementedError


class FirstHandler(Handler):
    def process(self, request: Request):
        if request.num == 1:
            return True


class SecondHandler(Handler):
    def process(self, request: Request):
        if request.num == 2:
            return True


class HandlerChain:
    handlers = []

    def addHandler(self, handler: Handler):
        self.handlers.append(handler)

    def process(self, request: Request):
        for handler in self.handlers:
            res = handler.process(request)
            if res is not None:
                print(handler)
                break


chain = HandlerChain()
chain.addHandler(FirstHandler())
chain.addHandler(SecondHandler())
chain.process(Request())
"""
使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。
将这些对象构成一条链，并沿着这条链传递该请求，直到触发某些条件结束。
"""
