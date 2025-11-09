# Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
# Concatenate the string with itself.
# Delete all the uppercase letters.
# Replace each vowel with '#'.
# You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.
# Note: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
# Input:
# A="aeiOUz"
# Output:
# "###z###z"

A=input()
A=A+A
A=''.join(ch for ch in A if not ch.isupper())
vowels='aeiou'
A=''.join('#' if ch in vowels else ch for ch in A)
print(A)