'''\nQuestion 34: Find common elements of two lists.\n'''\n\na=[1,2,3,4,5]
b=[3,4,5,6,7]
common=[]
for x in a:
    if x in b and x not in common: common.append(x)
print(common)\n