class R4C(object):
    def __init__(self, ammo):
        self.ammo = ammo
    
    def fire(self, bullets):
        if self.ammo >= bullets:
            self.ammo -= bullets
            print('Bullets fired:' + str(bullets))
        elif self.ammo == 0:
            print('Need to reload')
            self.reload()
        elif self.ammo < bullets:
            print('Bullets fired:' + str(self.ammo))
            self.ammo = 0

        print('Ammo count:' + str(self.ammo))
    
    def reload(self):
        if self.ammo >= 31:
            print('No need for reload')
        else:
            self.ammo = 31
            print('Reload completed')

# Testing class
g1 = R4C(31)
g1.fire(12)
print(g1.ammo)
g1.fire(20)
print(g1.ammo)
g1.fire(1)
