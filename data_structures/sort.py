# Sorting methods.
class sort():
    def __str__(self):
        return 'This is a class containing multiple sorting methods.'

    # Bubble sort.
    # Complexity: O(n^2)
    @classmethod
    def bubblesort(self, seq):
        flag = True
        r_seq = seq.copy()

        while flag :
            flag = False
            i = 0
            while i < len(r_seq) - 1:
                temp = r_seq[i]
                if r_seq[i] > r_seq[i+1] :
                    r_seq[i] = r_seq[i+1]
                    r_seq[i+1] = temp
                    flag = True
                i += 1
        
        return r_seq

    # Quick sort.
    # Complexity: O(nlogn)
    @classmethod
    def quicksort(self, seq, low, high):
        i = low
        j = high
        
        if low < high:
            base = seq[low]
            while i < j:
                while seq[j] > base and j > i:
                    j -= 1
                if j > i:
                    seq[i] = seq[j]
                    i += 1
                
                while seq[i] < base and i < j:
                    i += 1
                if i < j:
                    seq[j] = seq[i]
                    j -= 1
                
            seq[i] = base

            self.quicksort(seq, low, i-1)
            self.quicksort(seq, i+1, high)
    
    # Merge sort.
    # Complexity: O(nlogn)
    @classmethod
    def mergesort(self, seq):
        s_len = len(seq)

        # Merge small lists into one ordered sequence.
        def merge(left:list, right:list)->list :
            res = []
            i, j = 0, 0
            left_len = len(left)
            right_len = len(right)

            while i < left_len and j < right_len:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            if i == left_len:
                res += right[j:]
            elif j == right_len:
                res += left[i:]
            
            return res
                
        if s_len <= 1:
            return seq
        middle = s_len // 2

        # Recursively devide the sequence
        left = self.mergesort(seq[:middle])
        right = self.mergesort(seq[middle:])

        # Merge small lists into one ordered sequence.
        return merge(left, right)


if __name__ == '__main__':
    sample = [2, 3, 10, 1, 4, 7, 5, 9, 12, 0]
    print(sort.mergesort(sample))
