from zope.interface import Interface
from zope.interface import implementer


class ITest(Interface):

    def test(self):
        """test"""


@implementer(ITest)
class InstanceOne(object):

    def test(self):
        print("test1")


@implementer(ITest)
class InstanceTwo(object):

    def test(self):
        print("test2")


instance1 = InstanceOne()
print(instance1.test())
