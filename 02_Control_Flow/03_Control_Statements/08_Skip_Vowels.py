"""
Question:
Print a string without its vowels.
"""

text = "Programming"
vowels = "aeiou"

for character in text:
    if character.lower() in vowels:
        continue

    print(character, end="")

print()