def max(lst):
    mnum=lst[0]
    for p in lst:
        if p>mnum:
            mnum=p
    return mnum
list_of_mine=[4,5,6,2,4,35543]
print(max(list_of_mine))
