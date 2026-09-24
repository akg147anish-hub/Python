"""
Question:
Check whether a character is a vowel or consonant.
"""

character = input("Enter a character: ").lower()

if character in "aeiou":
    print("Vowel")
else:
    print("Consonant")