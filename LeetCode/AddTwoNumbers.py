'''
You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.
'''

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = [8, 4, 3, 5, 0]
l2 = [5, 6, 4, 7, 0]

result = []

for item in zip(l1, l2):
    result.append(item[0] + item[1])
    # if item[0] + item[1] < 10:
    #     result.append(item[0] + item[1])
    # else:

# if 0 in result:
#     result.index(0)

print(result)