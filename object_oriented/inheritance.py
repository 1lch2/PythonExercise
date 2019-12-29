import class_exception as ce
from types import MethodType

# AK-74M
class AKM(ce.AR):
    # Override.
    magsize = 40

    # Use __slots__ to limit the properties that can be bound with instance.
    __slots__ = ('rpm', '__airjab', 'testfunc', '_prop')

    def airjab(self):
        self.__airjab = 3
    
    def fire_airjab(self):
        if self.__airjab == 0:
            print('No more airjab.')
        else:
            self.__airjab -= 1
            print('Airjab deployed.')

    @property
    def getprop(self):
        self._prop = 'prop'
        return self._prop

def testfunc(self):
    print('Test function here.')

if __name__ == '__main__':
    # Test inheritance.
    AK = AKM(30)
    print(AK.checkmag())
    AK.airjab()
    AK.fire_airjab()
    AK.fire(23)
    print(AK.checkmag())
    print(AK.magsize)

    AK.rpm = 650
    print(AK.rpm)
    # print(dir(AK))

    # Test @property
    print(AK.getprop)

    # Test dynamically bind method with an instance.
    AK.testfunc = MethodType(testfunc, AK)
    AK.testfunc() # Ignore error in pylint, this actually works as intended.

    print(callable(AK.testfunc)) # Stupid pylint can`t even figure out it is callable.
