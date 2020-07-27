import math

# Searching methods.
class search:
    """Search algorithms.
    """
    def __str__(self):
        return 'This is a class containing multiple searching methods.'

    @classmethod
    def binsearch(self, seq: list, target: int, low: int, high: int) -> int:
        """Binary search.

        This method assumes that the target number is in the input sequence.

        Args:
            seq: Target sequence.
            target: Target number.
            low: Interval starting point.
            high: Interval ending point.
        
        Returns:
            The index of target in the sequence.
        """
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