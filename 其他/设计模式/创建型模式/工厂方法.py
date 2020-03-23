class Redis:
    pass


class RedisManager:
    redis = None

    @classmethod
    def getRedis(cls):
        if not cls.redis:
            cls.redis = Redis()
        return cls.redis


"""
定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method使一个类的实例化延迟到其子类

工厂方法可以隐藏创建产品的细节，且不一定每次都会真正创建产品，
完全可以返回缓存的产品，从而提升速度并减少内存消耗
"""
