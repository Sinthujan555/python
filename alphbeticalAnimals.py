animal1 = input("Enter First Animal: ")
animal2 = input("Enter Second Animal: ")

#Makes sure that the first letter is capitalised to make the sorting work
animal1 = animal1.capitalize()
animal2 = animal2.capitalize()

list = [animal1, animal2]
print(sorted(list))
