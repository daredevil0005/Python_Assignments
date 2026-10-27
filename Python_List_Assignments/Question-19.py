'''\nQuestion 19: Remove duplicates from 10 numbers.\n'''\n\na=[1,2,3,2,4,5,1,6,4,7]
unique=[]
for x in a:
    if x not in unique: unique.append(x)
print(unique)\n