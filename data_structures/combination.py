# Returns full combination of the input list.
# Reference: http://wuchong.me/blog/2014/07/28/permutation-and-combination-realize/
def comb(numlist:list):
    allset = []
    l_len = len(numlist)

    n = 1 << l_len
    for i in range(1, n):
        t_list = []
        for j in range(l_len):
            temp = i
            if temp & (1 << j):
                t_list.append(numlist[j])

        allset.append(t_list)

    return allset


# From comment in https://blog.csdn.net/destiny_python/article/details/77461518
def ZuHeIndex(li):
    reli = []
    for i in range(0, len(li)):
        if 0 == i:
            reli.append([i])
        else:
            addli = []
            addli.append([i])
            for ii in reli:
                addli.append(ii+[i])
            reli += addli
    return reli


if __name__ == '__main__':
    print(comb(['a', 'b', 'c']))
