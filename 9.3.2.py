def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mindpoint = len(alist) // 2
        if alist[mindpoint]== item:
            return True
        else:
            if item < alist[mindpoint]:
                return binarySearch(alist[:mindpoint], item)
            else:
                return binarySearch(alist[mindpoint+1:], item)
testlist = [0,1,2,8,13,17,19,32,42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))