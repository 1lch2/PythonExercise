# Customized exceptions.
class InitMagError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo


# Assualt rifle.
class AR(object):
    magsize = 30

    # Use __slots__ to limit the variables that can be bound with instance.
    __slots__ = ('__ammo')

    def __init__(self, ammo):
        try:
            if ammo > 30:
                self.__ammo = 30
                raise InitMagError("[Wrong ammo number.]")
        except InitMagError as e:
            print(e)
        else:
            self.__ammo = ammo
            print('AR created.')

    # Fire given number of bullets.
    def fire(self, bullets):
        if self.__ammo >= bullets:
            self.__ammo -= bullets
            print('Bullets fired:' + str(bullets))
        elif self.__ammo == 0:
            print('Need to reload')
            self.reload()
        elif self.__ammo < bullets:
            print('Bullets fired:' + str(self.__ammo))
            self.reload()

        print('Ammo count:' + str(self.__ammo))
    
    # Reload the gun to a full magzine with 30 rounds.
    def reload(self):
        if self.__ammo >= 30:
            print('No need for reload')
        else:
            self.__ammo = 30
            print('Reload completed')

    # Check magzine
    def checkmag(self):
        return self.__ammo

def test_main():
    # Testing class
    g1 = AR(31)
    g1.fire(12)
    print(g1.checkmag())
    g1.fire(20)
    print(g1.checkmag())
    g1.reload()
    g1.fire(1)

    print('-----------------------\n')
    # Testing exception.
    g2 = AR(50)
    print(g2.checkmag())

if __name__ == '__main__':
    test_main()
