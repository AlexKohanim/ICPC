s = input()
#print((len([x for x in s.split() if "ae" in x]),len(s.split())))
print("dae ae ju traeligt va" if (len([x for x in s.split() if "ae" in x]) / len(s.split())) >= 0.4 else "haer talar vi rikssvenska")
