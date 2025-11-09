# Write a program to input T strings (S) from user and print count of vowels and consonants in it.
# Input:
# 2
# List
# Apple
# Output:
# 1 3
# 2 3

T=int(input())
for i in range(T):
    S=input()
    vowels='aeiouAEIOU'
    vow_count=0
    cons_count=0

    for ch in S:
        if ch.isalpha():
            if ch in vowels:
                vow_count+= 1
            else:
                cons_count+= 1
    print(vow_count,cons_count)