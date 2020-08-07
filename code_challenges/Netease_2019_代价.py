# 你有3个需要完成的任务，完成这3个任务是需要付出代价的。
# 首先，你可以不花任何代价的完成一个任务；
# 然后，在完成了第i个任务之后，你可以花费|Ai - Aj|的代价完成第j个任务。|x|代表x的绝对值。
# 计算出完成所有任务的最小代价。

# 输入描述:
# 一行3个整数A1,A2,A3，每个数字之间用一个空格分隔。所有数字都是整数，并且在[1,100]范围内。

# 输出描述:
# 一个整数，代表最小的代价。

# 输入例子1:
# 1 6 3

# 输出例子1:
# 5

# 输入例子2:
# 10 10 10

# 输出例子2:
# 0

def calculateCost(data: list) -> int:
    delta = {} # 0: c-a, 1: a-b, 2: b-c
    for i in range(3):
        delta[i] = abs(int(data[i-1]) - int(data[i]))
    
    cost = 0
    cost_smallest = 65535
    for i in range(3):
        for j in range(3):
            if j == i:
                continue
            cost = delta[i] + delta[j]
            if cost <= cost_smallest:
                cost_smallest = cost
    return cost_smallest


if __name__ == "__main__":
    s = input()
    data = s.split()
    
    print(calculateCost(data))