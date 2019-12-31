# Submachine gun class.
class SMG(object):
    def __init__(self, magsize, rpm):
        self._magsize = magsize
        self._mag = magsize
        self._rpm = rpm

    @property
    def ammo(self):
        return self._mag

    @property
    def rpm(self):
        return self._rpm

    def fullauto(self, bullets):
        if bullets <= 0 or bullets > self._magsize:
            raise ValueError('Incorrect bullets count.')
        else:
            self._mag -= bullets
            print('Bullets fired: ' + str(bullets))

    def reload(self):
        if self._mag == self._magsize:
            print('No need for reload.')
        else:
            self._mag = self._magsize
            print('Reload complete.')


# Pistol class.
class HG(object):
    def __init__(self, magsize):
        self._magsize = magsize
        self._mag = magsize

    def __str__(self):
        return 'Pistol object (magsize: %d)' % self._magsize

    def semiauto(self):
        if self._mag == 0:
            raise ValueError('No bullet in magzine !')
        else:
            self._mag -= 1
            print('Bullets fired: 1.')

# Multi-inheritance test.
class SMG11(SMG, HG):
    pass

# Class object iteration.
class EXP(object):
    def __init__(self):
        self._base = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self._base = self._base * 2
        if self._base > 600:
            raise StopIteration()
        return self._base

    def __getitem__(self, n):
        return 2 ** n


def inheritance_test():
    # Multi-inheritance.
    g1 = SMG11(16, 1270)

    g1.fullauto(13)
    print(g1.ammo)
    g1.reload()

    print(g1.rpm)

    g1.semiauto()
    print(g1.ammo)


def customize_test():
    # Customized class with inner variables.
    g2 = HG(15)
    print(g2)

    e = EXP()
    for i in e:
        print(i)
    
    print(e[6])


if __name__ == '__main__':
    customize_test()
