word = input("Your Word Here: ")

vowels = ('a', 'e', 'i', 'o', 'u')

count = 0

for i in range(len(word)):
    if word[i] in vowels:
        count += 1

print("There are", count, "Vowels in", word)
