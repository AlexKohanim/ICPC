import string
for _ in range(int(input())):
    letters = list(string.ascii_lowercase)
    for c in input():
        if c.lower() in letters:
            letters.remove(c.lower())
    if len(letters) == 0:
        print("pangram")
    else:
        print("missing","".join([x for x in letters]))

