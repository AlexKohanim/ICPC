ref  = "welcome to code jam"
reflen = len(ref)


def recurrsive_counter(res, increm):
    cols = 0
    if increm == reflen -1: # base case
        for r in res:
            if r == "m":
                cols += 1
        return cols
    for i, s in enumerate(res):
        if s == ref[increm]:
            cols += recurrsive_counter(res[i +1:], increm +1)
    return cols

for n in range(int(input())):
    print("Case #" + str(n+1) + ":", end = " ")
    count = recurrsive_counter(input(), 0)
    if count < 1000:
        print(str(count).zfill(4))
    else:
        print(str(count)[len(str(count))-5:])
    
    
        
