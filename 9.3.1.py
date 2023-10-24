def binarySearch(alist, item):
    frist = 0
    last = len(alist)-1
    found = False

    while frist <= last and not found:
        mindpoint = (frist + last)//2
        if alist[mindpoint] == item:
            found = True
        else:
            frist = mindpoint+1
    return found
testlist = [1,2,8,13,17,19,32,42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))