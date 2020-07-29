# Sorting methods.
class Sort():
    def __str__(self):
        return 'This is a class containing multiple sorting methods.'

    @classmethod
    def bubblesort(cls, seq: list):
        """Bubble sort. Complexity: O(n^2).

        Returns: 
            The sorted sequence.
        """
        flag = True # 是否发生交换
        while flag :
            flag = False # 若一趟下来没有发生交换，则 flag 保持 False
            i = 0
            while i < len(seq) - 1:
                if seq[i] > seq[i+1] :
                    seq[i], seq[i+1] = seq[i+1], seq[i]
                    flag = True
                i += 1
        
        return seq


    @classmethod
    def quicksort(cls, seq: list, low: int, high: int):
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
        
        if low < high: #* 递归终止条件：左右端下标相遇
            base = seq[low] # 以左端起始的数字为枢轴
            while i < j: # 当左右侧指针相遇时停止循环
                while seq[j] > base and j > i: # 从右向左扫描比枢轴小的数
                    j -= 1 # j 向左移动一位
                if i < j: # 若左右指针相遇则不进行交换
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
    

    @classmethod
    def mergesort(cls, seq: list):
        """Two-way merge sort. Complexity: O(nlogn)

        Returns:
            The sorted sequence.
        """
        # Merge small lists into one ordered sequence.
        def merge(left: list, right: list) -> list :
            res = []
            i, j = 0, 0 # 左右列表的下标
            left_len = len(left)
            right_len = len(right)

            while i < left_len and j < right_len:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            # 当某一列表并归完后，合并另一个列表的剩余元素
            if i == left_len:
                res += right[j:]
            elif j == right_len:
                res += left[i:]
            return res

        s_len = len(seq)
        if s_len <= 1:
            return seq
        middle = s_len // 2

        # Recursively devide the sequence
        left = self.mergesort(seq[:middle])
        right = self.mergesort(seq[middle:])

        # Merge small lists into one ordered sequence.
        return merge(left, right)

    @classmethod
    def simple_select_sort(cls, seq: list):
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
    
    @classmethod
    def heap_sort(cls, seq: list):
        """Max heap sort. Complexity: O(nlogn).

        Args:
            seq: The input sequence.
            n: The length of the sequence.
        """
        def maxHeap(seq: list, size: int, i: int):
            # 从0开始的下标
            largest = i # 当前最大的节点（根节点）下标
            l = 2 * i + 1 # 左节点下标
            r = 2 * i + 2 # 右节点下标

            # 下标不能超出范围
            if l < size and seq[largest] < seq[l]: # 若左节点大于当前最大的节点，将largest指向 左 节点
                largest = l
            if r < size and seq[largest] < seq[r]: # 若右节点大于当前最大的节点，将largest指向 右 节点
                largest = r
            if largest != i: # 若有子节点比父节点大，则交换最大的节点到根节点
                seq[i], seq[largest] = seq[largest], seq[i]
                maxHeap(seq, size, largest) # 递归对调整后的二叉树进行检测调整

        n = len(seq)
        # 建立初始大顶堆
        for i in range(n, -1, -1): # 从后往前遍历
            maxHeap(seq, n, i)

        # 换出根节点的值并将其放入最终位置
        for i in range(n-1, 0, -1): # 从 倒数第二个位置开始，将已经排到最后的元素排除
            seq[0], seq[i] = seq[i], seq[0] # 此步将位于第一位的最大元素换到最后
            maxHeap(seq, i, 0) # 在减少了一个关键字的序列中进行调整


if __name__ == '__main__':
    sample = [2, 3, 10, 1, 4, 7, 5, 9, 12, 0, 30, 8]

    s = sample.copy()
    Sort.quicksort(s, 0, len(s)-1)
    print(s)

    s = sample.copy()
    Sort.simple_select_sort(s)
    print(s)

    s = sample.copy()
    Sort.heap_sort(s)
    print(s)

