def orderedsequentialSearch(alist, item):
    pos = 0 
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found
testlist = [0,1,2,8,13,17,19,32,42]
print(orderedsequentialSearch(testlist, 3))
print(orderedsequentialSearch(testlist, 13))