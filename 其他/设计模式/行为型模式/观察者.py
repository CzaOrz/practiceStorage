class Product:
    def __init__(self, p):
        self.p = p
        self.value = None


class Store:
    observers = []
    products = {}

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def addNewProduct(self, name, product):
        p = Product(product)
        self.products[name] = p
        for observer in self.observers:
            observer.onPublished(p)

    def setProduct(self, name, value):
        p = self.products[name]
        p.value = value
        for observer in self.observers:
            observer.onPriceChanged(p)


"""
定义对象之间一对多的依赖关系，当一个对象的状态发生改变的时候，
所以依赖于他的对象都将得到通知并更新
"""
