n = int(input("Alphabet Counter\nEnter the number of strings to input to list: "))

inplist = list()
chdict = dict()
for i in range(n):
    inp = input(f"Enter string {i + 1}: ")
    inplist.append(inp);
for word in inplist:
    for char in word.lower():
        if char.isalpha():
            chdict[char] = chdict.get(char, 0) + 1;

print("\nInput list is:", inplist, "\nOutput character count:", chdict)



