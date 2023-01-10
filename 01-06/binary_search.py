import bisect

mylist = [1,2,3,4,5,6,7]
print(bisect.bisect(mylist, 3))

def binary_search_recusion(target, start, end, data):
    if start > end:
        return False
    