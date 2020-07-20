# Sorting methods.
class Sort():
    def __str__(self):
        return 'This is a class containing multiple sorting methods.'

    @classmethod
    def bubblesort(self, seq: list):
        """Bubble sort. Complexity: O(n^2).

        Returns: 
            The sorted sequence.
        """
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


    @classmethod
    def quicksort(self, seq: list, low: int, high: int):
        """Quick sort in recursive method. Complexity: O(nlogn).

        Args:
            seq: The input sequence.
            low: Starting index of the (sub)seqence.
            high： Ending sequence of the (sub)sequence.
        
        Returns:
            No returns, the method operates on the original sequence.
        """
        i = low
        j = high
        
        if low < high: # 递归终止条件：左右端下标相遇
            base = seq[low] # 以左端起始的数字为枢轴
            while i < j: # 当左右侧指针相遇时停止循环
                while seq[j] > base and j > i: # 从右向左扫描比枢轴小的数
                    j -= 1 # j 向左移动一位
                if j > i:
                    seq[i] = seq[j] # 将比枢轴小的数放到 i 所指的位置
                    i += 1 # i 右移一位
                
                while seq[i] < base and i < j: # 交换方向，从左向右扫描比枢轴大的数
                    i += 1 # i 向右移动一位
                if i < j:
                    seq[j] = seq[i] # 将比枢轴大的数放到 j 所指的位置
                    j -= 1 # j 左移一位
                
            seq[i] = base # 将枢轴放在最终的位置

            self.quicksort(seq, low, i-1) # 递归对枢轴左侧排序
            self.quicksort(seq, i+1, high) # 递归对枢轴右侧排序
    
    # Merge sort.
    # Complexity: O(nlogn)
    @classmethod
    def mergesort(self, seq: list):
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

    @classmethod
    def simple_select_sort(self, seq: list):
        """Simple select sort. Complexity: O(n^2).

        Returns: 
            No returns, the method operates on the original sequence.
        """
        i, j, k = 0, 0, 0
        # i 为有序部分的末尾
        while i < len(seq):
            k = i       # k 为最小值下标
            j = i + 1   # j 为无序部分的开始

            # 该循环从无序序列中找到最小值
            while j < len(seq):
                if seq[k] > seq[j]: # seq[k] 为最小值时，k 不会再变化
                    k = j
                j += 1
            
            # 最小关键字和无序部分第一个值交换
            seq[i], seq[k] = seq[k], seq[i]

            i += 1
    
    # Heap sort
    # O(nlogn)
    def heap_sort(self, seq: list):
        pass

if __name__ == '__main__':
    sample = [2, 3, 10, 1, 4, 7, 5, 9, 12, 0, 30, 8]
    s = sample.copy()
    Sort.quicksort(s, 0, len(s)-1)
    print(s)

    s = sample.copy()
    Sort.simple_select_sort(s)
    print(s)
