#!/usr/bin/env python3


# Not Finished as of 12/2/18

correct = int(input())
my_answers = input()
f_answer = input()
diff = 0
total = len(my_answers)
my_correct = 0

# you can get up to n points for the same, then you can get m points for diff
# m = tot - n

# case1 dif > correct
# diff - correct

# total = diff + same

# case2 dif < correct
# correct + diff
#print(my_answers)
for i in range(total):
    if my_answers[i] != f_answer[i]:
        diff += 1
same = total - diff

if same <= correct:
    my_correct += same
else:
    my_correct += total - abs(correct - same)
my_correct = diff - correct

print(my_correct)