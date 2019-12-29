import class_exception

# AK-74M
class AKM(class_exception.AR):
    def airjab(self):
        self.__airjab = 3
    
    def fire_airjab(self):
        if self.__airjab == 0:
            print('No more airjab.')
        else:
            self.__airjab -= 1
            print('Airjab deployed.')

if __name__ == '__main__':
    AK = AKM(30)
    print(AK.checkmag())
    AK.airjab()
    AK.fire_airjab()
    AK.fire(23)
    print(AK.checkmag())
    