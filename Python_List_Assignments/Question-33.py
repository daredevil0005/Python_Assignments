'''\nQuestion 33: Find second largest distinct number.\n'''\n\na=[10,40,20,50,30]
unique=sorted(set(a))
if len(unique)>=2: print(unique[-2])
else: print("No second largest distinct number")\n