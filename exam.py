#!/usr/bin/env python3

correct = int(input())
my_answers = input()
f_answer = input()
diff = 0
total = len(my_answers)
my_correct = 0

for i in range(total):
    if my_answers[i] != f_answer[i]:
        diff += 1
same = total - diff

overflow = same - correct
if overflow >= 0:
    my_correct = total - overflow
else:
    my_correct = total + overflow
print(my_correct)