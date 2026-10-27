'''\nQuestion 40: Demonstrate list methods.\n'''\n\na=[30,10,20,10]
print("Original:",a)
a.append(40); print("append:",a)
a.extend([50,60]); print("extend:",a)
a.insert(1,15); print("insert:",a)
a.remove(10); print("remove:",a)
print("pop removed:",a.pop()); print("After pop:",a)
print("copy:",a.copy())
print("count 10:",a.count(10))
print("index 20:",a.index(20))
a.sort(); print("sort:",a)
a.reverse(); print("reverse:",a)
a.clear(); print("clear:",a)\n