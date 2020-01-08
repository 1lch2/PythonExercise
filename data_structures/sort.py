# Sorting methods.
class sort(object):
    def __str__(self):
        return 'This is a class containing multiple sorting methods.'

    # Bubble sort.
    # Complexity: O(n^2)
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
