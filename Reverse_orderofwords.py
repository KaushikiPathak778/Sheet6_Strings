# You are given string (A) and you have to print the reverse order of words.
# Input:
# Suyash Chaudhary
# Output:
# Chaudhary Suyash

A=input()
words=A.split()
reversed_words=words[::-1]
print(' '.join(reversed_words))
