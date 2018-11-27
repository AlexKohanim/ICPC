charsz = [" ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
chars = "abcddeeffggghhhiiijjjjkkkkllllmmmmmnnnnnoooooppppppqqqqqqrrrrrrsssssstttttttuuuuuuuvvvvvvvwwwwwwwwxxxxxxxxyyyyyyyyzzzzzzzz"
for n in range(int(input())):
    pos = -1
    print("Case #", n+1, ": ",sep = '', end = '')
    for c in input():
        posx = chars.count(c)
        if posx == pos:
            print(" ", end = '')
        d = charsz[posx].find(c) + 1 
        print("0" if posx == 0 else str(posx+1)*d, end = '')
        pos = posx 
    print()
