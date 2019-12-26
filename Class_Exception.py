# Customized exceptions.
class InitMagError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo


# Remington R4-C short barrel assualt rifle.
class R4C(object):
    def __init__(self, ammo):
        try:
            if ammo > 30:
                self.ammo = 30
                raise InitMagError("[Wrong ammo number.]")
        except InitMagError as e:
            print(e)
        else:
            self.ammo = ammo
            print('R4C created.')

    # Fire given number of bullets.
    def fire(self, bullets):
        if self.ammo >= bullets:
            self.ammo -= bullets
            print('Bullets fired:' + str(bullets))
        elif self.ammo == 0:
            print('Need to reload')
            self.reload()
        elif self.ammo < bullets:
            print('Bullets fired:' + str(self.ammo))
            self.reload()

        print('Ammo count:' + str(self.ammo))
    
    # Reload the gun to a full magzine with 30 rounds.
    def reload(self):
        if self.ammo >= 30:
            print('No need for reload')
        else:
            self.ammo = 30
            print('Reload completed')

# Testing class
g1 = R4C(31)
g1.fire(12)
print(g1.ammo)
g1.fire(20)
print(g1.ammo)
g1.reload()
g1.fire(1)

print('\n-----------------------\n')
# Testing exception.
g2 = R4C(50)
print(g2.ammo)