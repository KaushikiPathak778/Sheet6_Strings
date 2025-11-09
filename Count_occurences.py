# Find the number of occurrences of bob in string A consisting of lowercase English alphabets.
# Input:
# "abobc"
# Output:
# 1

A=input()
count=0
for i in range(len(A)-2):
    if A[i:i+3]=="bob":
        count+= 1
print(count)