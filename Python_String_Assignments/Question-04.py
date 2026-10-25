'''
count vowels in a string
'''
text = input("Enter a string: ")
count = sum(1 for ch in text.lower() if ch in "aeiou")
print("Number of vowels:", count)
