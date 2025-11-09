# Write a program to reverse the words present in a string. Check example input/output.
# Input:
# Everyone loves data science
# Output:
# enoyrevE sevol atad ecneics

A=input()
words=A.split()
reversed_words=[]
for word in words:
    reversed_words.append(word[::-1])
print(' '.join(reversed_words))