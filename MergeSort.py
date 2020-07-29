# Andre Doumad

def MergeSort(n):
    if len(n) > 1:
        i_mid = len(n)//2
        leftList = n[:i_mid]
        rightList = n[i_mid:]

        MergeSort(leftList)
        MergeSort(rightList)

        i_left=i_right=i_new = 0

        while i_left < len(leftList) and i_right < len(rightList):
            if leftList[i_left] < rightList[i_right]:
                n[i_new] = leftList[i_left]
                i_left+=1
            else:
                n[i_new] = rightList[i_right]
                i_right+=1
            i_new+=1
        
        while i_left < len(leftList):
            n[i_new] = leftList[i_left]
            i_left+=1
            i_new+=1
        
        while i_right < len(rightList):
            n[i_new] = rightList[i_right]
            i_right+=1
            i_new+=1
        return n
# O(nlogn)
print(MergeSort([12,99,33,22,100,44,2,0,1,200,300,233,428,5]))
# output: [0, 1, 2, 5, 12, 22, 33, 44, 99, 100, 200, 233, 300, 428]