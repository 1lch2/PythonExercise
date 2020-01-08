import math

# Searching methods.
class search(object):
    def __str__(self):
        return 'This is a class containing multiple searching methods.'

    # Binary search.
    @classmethod
    def binsearch(self, seq, target, low, high):
        # Return at every recursion in order to get proper result.
        try:
            if target > seq[high-1] or target < seq[0]:
                raise ValueError('No match in this sequence.')
            else:
                if high - low > 1:
                    mid = math.floor((high - low)/2)
                    if target < seq[mid]:
                        return self.binsearch(seq, target, low, mid)
                    elif target > seq[mid]:
                        return self.binsearch(seq, target, mid, high)
                    elif target == seq[mid]:
                        return mid
        except BaseException as e:
            print(e)


def test():
    seq = [1,2,3,4,5,6,7,8,9,10,11]
    target = 3
    low = 0
    high = len(seq)

    loc = search.binsearch(seq, target, low, high)

    print(loc)
    print(seq[loc])

if __name__ == '__main__':
    test()