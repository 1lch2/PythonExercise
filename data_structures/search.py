import math

# Searching methods.
class Search:
    """Search algorithms.
    """
    def __str__(self):
        return 'This is a class containing multiple searching methods.'

    @classmethod
    def binsearch_recur(cls, seq: list, target: int, low: int, high: int) -> int:
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
                mid = (high - low) // 2
                if target < seq[mid]:
                    return cls.binsearch(seq, target, low, mid)
                elif target > seq[mid]:
                    return cls.binsearch(seq, target, mid, high)
                elif target == seq[mid]:
                    return mid
        
    @classmethod
    def binsearch_iter(cls, seq: list, target: int) -> int:
        """Non-recursive binary search algorithm.

        Args:
            seq: The sorted list.
            target: The target number.
        
        Returns:
            If target is in the list, returns the index.
            Otherwise, returns the index that target will be inserted into.
        """
        low = 0
        high = len(seq) - 1

        while low <= high: # 左右指针交叉后截止
            middle = (high + low) // 2

            if target < seq[middle]:
                high = middle - 1
            elif target > seq[middle]:
                low = middle + 1
            elif target == seq[middle]:
                return middle
                        
        if seq[middle] >= target:
            return middle
        else:
            return middle+1


def test():
    seq = [1,3,5,6]
    target = 2
    # low = 0
    # high = len(seq)

    loc = Search.binsearch_iter(seq, target)

    print(loc)

if __name__ == '__main__':
    test()