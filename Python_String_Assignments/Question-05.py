'''
count consonants in a string
'''
text = input("Enter a string: ")
count = sum(1 for ch in text.lower() if ch.isalpha() and ch not in "aeiou")
print("Number of consonants:", count)
